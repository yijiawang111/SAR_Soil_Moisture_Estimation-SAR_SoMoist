import numpy as np  
import csv
from Ui_login import Ui_Form
from Ui_Module2 import Ui_retrieval
from Ui_Module1 import Ui_mainwindow
from Ui_Module3 import Ui_TimeSeries
from PySide6.QtWidgets import ( QApplication,QLabel, QDialog,  
                               QVBoxLayout,  QWidget, QMessageBox, QFileDialog, QGraphicsView,
                               QGraphicsScene, QComboBox, QLineEdit)
from PySide6.QtCore import QTimer,  Qt, QRect,   QEvent, QObject, QPoint, Signal
from datetime import datetime
from PySide6.QtGui import QPixmap, QPainter, QImage, QWheelEvent, QBitmap 
import os
from osgeo import gdal  
import matplotlib.pyplot as plt  
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas  
from qfluentwidgets import Dialog, InfoBar, InfoBarPosition  
from qfluentwidgets import SplitFluentWindow, FluentIcon  
from matplotlib.colors import Normalize 
from matplotlib.figure import Figure
from matplotlib.cm import ScalarMappable  
import subprocess
from scipy.ndimage import gaussian_filter  # Used for Gaussian blur interpolation
from osgeo import gdal

# Enable exception handling
gdal.UseExceptions()

# Custom signal
custom_signal = Signal()

plt.rcParams['font.sans-serif'] = ['Arial'] # Display English
plt.rcParams['axes.unicode_minus'] = False   

class login(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()  # Initialize the parent object
        self.ui = Ui_Form()  # Instantiate the Ui_Form class in pyside_ui_to_code
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setFixedSize(self.size())  # Lock the window size
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)  # Keep the window centered

        self.ui.Main_Login.clicked.connect(self.open_child_window)
        self.ui.Main_exit.clicked.connect(self.close)

        self.dragging = False
        self.offset = QPoint()

        self.ui.lineEdit.setText("SARmates_Member")
        self.ui.lineEdit_2.setText("NISAR_Program")

    def showDialog(self):
        title = 'Warning'
        content = """The password is wrong, please enter a right one or you have no permission to access the SAR-SoMoist."""
        w = Dialog(title, content, self)  # Create a dialog box
        if w.exec():  # Display the dialog box and wait for user selection
            print('Yes ')  
        else:
            print('Cancel ')  
    
    def open_child_window(self):
        if self.ui.lineEdit.text() == "SARmates_Member" and \
                self.ui.lineEdit_2.text() == "NISAR_Program":
            self.SOMT_window = navigation()  # Display the main interface
            self.SOMT_window.show()
            self.close()
        else:
            self.showDialog() 

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.globalPosition().toPoint() - self.pos()
    
    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(event.globalPosition().toPoint() - self.offset)
    
    def mouseReleaseEvent(self, event):
        self.dragging = False

class AppController:  # Create a controller to implement mutual reading between classes
    def __init__(self):
        self.main_window = None
        self.retrieval_window = None
        
class Mainwindow(QWidget, Ui_mainwindow):
    def __init__(self, controller, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        
        self.controller = controller
        self.controller.main_window = self  # Register itself to the controller

        # Pseudo-color map selection dropdown box
        self.cmap_combo = QComboBox()
        self.cmap_combo.addItems(['jet', 'viridis', 'hot', 'cool', 'rainbow', 'terrain'])
        # Set the background color and font color of the dropdown box
        self.cmap_combo.setStyleSheet("""
            QComboBox {
            background-color: rgb(255, 255, 255);
            color:rgb(0,0,0);
            border: 1px solid #4a90e2;
            border-radius: 4px;
            padding: 2px 10px 2px 10px;
            }
            QComboBox QAbstractItemView {
            color:rgb(0,190,190); /* Dropdown list background color */
            background-color:rgb(255,255,255);     /* Dropdown list font color */           
            selection-background-color: #4a90e2;
            selection-color: #ffffff;
            }
        """)
        self.cmap_combo.setCurrentText('jet')
        color_label = QLabel("Pseudo-color map:")
        color_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)  # Right-align and center vertically
        self.horizontalLayout_18.addWidget(color_label)
        self.horizontalLayout_18.addWidget(self.cmap_combo)
        # Smooth parameter setting
        smooth_label = QLabel("Smoothing level:")
        smooth_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)  # Right-align and center vertically
        self.horizontalLayout_18.addWidget(smooth_label)
        self.smooth_combo = QComboBox()
        self.smooth_combo.addItems(["Very low", "Low", "Medium", "High", "Very high", "Custom (0.1-5)"])
        self.smooth_combo.setStyleSheet("""
            QComboBox {
            background-color: rgb(255, 255, 255);
            color:rgb(0,0,0);
            border: 1px solid #4a90e2;
            border-radius: 4px;
            padding: 2px 10px 2px 10px;
            }
            QComboBox QAbstractItemView {
            color:rgb(0,190,190); /* Dropdown list background color */
            background-color:rgb(255,255,255);     /* Dropdown list font color */           
            selection-background-color: #4a90e2;
            selection-color: #ffffff;
            }
        """)

        self.smooth_combo.setCurrentText("Medium")
        self.horizontalLayout_18.addWidget(self.smooth_combo)
        
        self.sigma_input = QLineEdit()
        self.sigma_input.setPlaceholderText("Gaussian kernel size (0.1-5)")
        self.sigma_input.setText("1.2")  # Default value
        self.horizontalLayout_18.addWidget(self.sigma_input)
        
        # Connect signals to control the enable state of the input box
        self.smooth_combo.currentTextChanged.connect(self.update_sigma_enabled)
        self.update_sigma_enabled(self.smooth_combo.currentText())  # Initialize the state

        # Call after all controls are added to the layout
        self.horizontalLayout_18.setStretch(0, 1)  # Pseudo-color map label
        self.horizontalLayout_18.setStretch(1, 3)  # Pseudo-color map dropdown box
        self.horizontalLayout_18.setStretch(2, 1)  # Smoothing level label
        self.horizontalLayout_18.setStretch(3, 3)  # Smoothing level dropdown box
        self.horizontalLayout_18.setStretch(4, 3)  # Input box

        self.current_render_type = None

        self.SAR_path_select.clicked.connect(self.choose_SAR_file)
        self.Passive_path_select_2.clicked.connect(self.choose_Passive_min_file)
        self.Passive_path_select_3.clicked.connect(self.choose_Passive_max_file)
        self.SARINC_path_select_3.clicked.connect(self.choose_SARINC_file)
        
        # Pseudo-color rendering button, automatically apply filtering when clicked
        self.Pseudo_color_rendering_1.clicked.connect(lambda: self.render_SAR_pseudo_color(True))
        self.Pseudo_color_rendering_4.clicked.connect(lambda: self.render_SARINC_pseudo_color(True))
        self.Pseudo_color_rendering_2.clicked.connect(lambda: self.render_Passive_min_pseudo_color(True))
        self.Pseudo_color_rendering_3.clicked.connect(lambda: self.render_Passive_max_pseudo_color(True))
        
        # Initialize dragging and event filters
        self.drag_data = {}
        self.views = [self.graphicsView, self.graphicsView_2, self.graphicsView_3, self.graphicsView_10]
        for view in self.views:
            self.drag_data[view] = {"start_pos": None, "is_dragging": False}
            view.viewport().installEventFilter(self)
            # Enable anti-aliasing and smooth scaling
            view.setRenderHint(QPainter.Antialiasing, True)
            view.setRenderHint(QPainter.SmoothPixmapTransform, True)

    def update_sigma_enabled(self, text):
        """Enable or disable the sigma input box according to the smoothing level selection"""
        self.sigma_input.setEnabled(text == "Custom (0.1-5)")
        if text != "Custom (0.1-5)":
            # Set the default sigma value according to the selection
            if text == "Very low":
                self.sigma_input.setText("0.3")
            elif text == "Low":
                self.sigma_input.setText("0.8")
            elif text == "Medium":
                self.sigma_input.setText("1.2")
            elif text == "High":
                self.sigma_input.setText("2.0")
            elif text == "Very high":
                self.sigma_input.setText("3.5")
            self.sigma_input.setStyleSheet("background-color: #f0f0f0;")
        else:
            self.sigma_input.setStyleSheet("background-color: white;")
    
    def create_colorbar(self, min_val, max_val, cmap_name, target_widget):
        """Create a colorbar and display it in the specified widget"""
        # Clear the original content of the target widget
        layout = target_widget.layout()
        if layout:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
        else:
            layout = QVBoxLayout(target_widget)
            layout.setContentsMargins(0, 0, 0, 0)
            target_widget.setLayout(layout)
    
        # Create a figure and axes
        fig = Figure(figsize=(1, 3))
        canvas = FigureCanvas(fig)
        ax = fig.add_axes([0, 0, 1, 1])  # Adjust the position and size
    
        # Set the colormap
        cmap = plt.get_cmap(cmap_name)
        norm = Normalize(vmin=min_val, vmax=max_val)
    
        # Create a colorbar
        cb = fig.colorbar(
            ScalarMappable(norm=norm, cmap=cmap),
            cax=ax,
            orientation='vertical'
        )
    
        # Customize the colorbar appearance
        cb.ax.set_title('')  # Remove the title
        cb.ax.tick_params(axis='both', which='both', length=0)  # Remove tick marks
        cb.ax.set_xticks([])  # Remove x-axis ticks
        cb.ax.set_yticks([])  # Remove y-axis ticks
    
        # Add the canvas to the target widget
        layout.addWidget(canvas)
        canvas.draw()
    
        return canvas
    
    def get_sigma_value(self):
        """Get the currently selected sigma value"""
        smooth_level = self.smooth_combo.currentText()
        if smooth_level == "Custom (0.1-5)":
            try:
                sigma = float(self.sigma_input.text())
                if 0.1 <= sigma <= 5:
                    return sigma
                else:
                    InfoBar.error(
                        title='Parameter range warning',
                        content="The Gaussian kernel size should be between 0.1 and 5, and has been automatically adjusted to the default value",
                        orient=Qt.Horizontal,
                        isClosable=True,
                        position=InfoBarPosition.TOP,
                        duration=3000,
                        parent=self
                    )
                    return 1.2
            except ValueError:
                InfoBar.error(
                    title='Parameter error',
                    content="Please enter a valid number, and the default value has been automatically used",
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP_LEFT,
                    duration=3000,
                    parent=self
                )
                return 1.2
        # Preset value mapping
        sigma_map = {
            "Very low": 0.3,
            "Low": 0.8,
            "Medium": 1.2,
            "High": 2.0,
            "Very high": 3.5
        }
        return sigma_map.get(smooth_level, 1.2)

    def eventFilter(self, source: QObject, event: QEvent) -> bool:
        "Event filter to handle mouse dragging logic"
        view_map = {view.viewport(): view for view in self.views}
        view = view_map.get(source)
    
        if view is None:
            return super().eventFilter(source, event)
    
        if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
            self.drag_data[view]["start_pos"] = event.pos()
            self.drag_data[view]["is_dragging"] = True
            view.setCursor(Qt.ClosedHandCursor)
            return True
        
        elif event.type() == QEvent.MouseMove:
            drag_info = self.drag_data[view]
            if drag_info["is_dragging"] and drag_info["start_pos"]:
                delta = event.pos() - drag_info["start_pos"]
                drag_info["start_pos"] = event.pos()
                h_bar = view.horizontalScrollBar()
                v_bar = view.verticalScrollBar()
                h_bar.setValue(h_bar.value() - delta.x())
                v_bar.setValue(v_bar.value() - delta.y())
                return True
        
        elif event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
            self.drag_data[view] = {"start_pos": None, "is_dragging": False}
            view.setCursor(Qt.ArrowCursor)
            return True 
        
        return super().eventFilter(source, event)

    # ---------------------- File selection functions ----------------------
    def choose_SAR_file(self):
        """Select a SAR file and save the path, and clear the filtering range at the same time"""
        filename, _ = QFileDialog.getOpenFileName(self, 'Open SAR file', '', 'All files (*)')
        if filename:
            self.textBrowser.setText(filename)
            InfoBar.success(
                title='STEP1: SAR File Selected Successfully!',
                content=f'The selected file path is: {filename}',
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,  # Custom position
                duration=2500,
                parent=self
            )


    def choose_Passive_min_file(self):
        """Select a Passive Min file and save the path, and clear the filtering range at the same time"""
        filename, _ = QFileDialog.getOpenFileName(self, 'Open Passive Min file', '', 'All files (*)')
        if filename:
            self.textBrowser_2.setText(filename)
            InfoBar.success(
                title='STEP2: Passive Min File Selected Successfully!',
                content=f'The selected file path is: {filename}',
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,  # Custom position
                duration=2500,
                parent=self
            )
    
    def choose_Passive_max_file(self):
        """Select a Passive Max file and save the path, and clear the filtering range at the same time"""
        filename, _ = QFileDialog.getOpenFileName(self, 'Open Passive Max file', '', 'All files (*)')
        if filename:
            self.textBrowser_4.setText(filename)
            InfoBar.success(
                title='STEP3: Passive Max File Selected Successfully!',
                content=f'The selected file path is: {filename}',
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,  # Custom position
                duration=2500,
                parent=self
            )

    def choose_SARINC_file(self):
        """Select a SAR incidence angle file and save the path, and clear the filtering range at the same time"""
        filename, _ = QFileDialog.getOpenFileName(self, 'Open SAR incidence angle file', '', 'All files (*)')
        if filename:
            self.textBrowser_3.setText(filename)
            InfoBar.success(
                title='STEP4: SARINC File Selected Successfully!',
                content=f'The selected file path is: {filename}',
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,  # Custom position
                duration=2500,
                parent=self
            )

    # ---------------------- Pseudo-color rendering functions ----------------------
    def render_SAR_pseudo_color(self, set_render_type=False):
        """SAR data rendering"""
        if set_render_type:
            self.current_render_type = "SAR"
        file_path = self.textBrowser.toPlainText()
        if not file_path:
            InfoBar.error(
                        title='Error!',
                        content="You have not selected a SAR file path!",
                        orient=Qt.Horizontal,
                        isClosable=True,
                        position=InfoBarPosition.TOP_LEFT,
                        duration=4000,    # won't disappear automatically
                        parent=self
                                        )
            return
        
        # Get the maximum and minimum values and smoothing parameters input by the user
        try:
            min_val = float(self.SAR_min.text()) if self.SAR_min.text() else None
            max_val = float(self.SAR_max.text()) if self.SAR_max.text() else None
            if min_val is not None and max_val is not None and min_val >= max_val:
                QMessageBox.warning(self, "Input error", "The minimum value must be less than the maximum value")
                return
            sigma = self.get_sigma_value()
        except ValueError:
            QMessageBox.warning(self, "Input error", "Please enter a valid number")
            return
        
        # Rendering logic
        self.graphicsView.setStyleSheet("QGraphicsView { background-color: black; }")
        scene, data_min, data_max = self.load_raster(file_path, min_val, max_val, sigma)
        self.graphicsView.setScene(scene)
        self.SAR_min.setText(str(round(data_min, 3)))
        self.SAR_max.setText(str(round(data_max, 3)))
        self.graphicsView.fitInView(scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
        self.create_colorbar(
            min_val=float(self.SAR_min.text()),
            max_val=float(self.SAR_max.text()),
            cmap_name=self.cmap_combo.currentText(),
            target_widget=self.label_2)
    
    def render_SARINC_pseudo_color(self, set_render_type=False):
        """SAR incidence angle rendering"""
        if set_render_type:
            self.current_render_type = "SARINC"
        file_path = self.textBrowser_3.toPlainText()
        if not file_path:
            InfoBar.error(
                        title='Error!',
                        content="You have not selected a SARINC file path!",
                        orient=Qt.Horizontal,
                        isClosable=True,
                        position=InfoBarPosition.TOP_LEFT,
                        duration=4000,    # won't disappear automatically
                        parent=self
                                        )
            return
        
        # Get the maximum and minimum values and smoothing parameters input by the user
        try:
            min_val = float(self.SARInc_min.text()) if self.SARInc_min.text() else None
            max_val = float(self.SARInc_max.text()) if self.SARInc_max.text() else None
            if min_val is not None and max_val is not None and min_val >= max_val:
                QMessageBox.warning(self, "Input error", "The minimum value must be less than the maximum value")
                return
            sigma = self.get_sigma_value()
        except ValueError:
            QMessageBox.warning(self, "Input error", "Please enter a valid number")
            return
        
        self.graphicsView_2.setStyleSheet("QGraphicsView { background-color: black; }")
        scene, data_min, data_max = self.load_raster(file_path, min_val, max_val, sigma)
        self.graphicsView_2.setScene(scene)
        self.SARInc_min.setText(str(round(data_min, 3)))
        self.SARInc_max.setText(str(round(data_max, 3)))
        self.graphicsView_2.fitInView(scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
        self.create_colorbar(
                min_val=float(self.SARInc_min.text()),
                max_val=float(self.SARInc_max.text()),
                cmap_name=self.cmap_combo.currentText(),
                target_widget=self.label_9
            )
    
    def render_Passive_min_pseudo_color(self, set_render_type=False):
        """Passive Min rendering"""
        if set_render_type:
            self.current_render_type = "PassiveMin"
        file_path = self.textBrowser_2.toPlainText()
        if not file_path:
            InfoBar.error(
                        title='Error!',
                        content="You have not selected a Passive Min file path!",
                        orient=Qt.Horizontal,
                        isClosable=True,
                        position=InfoBarPosition.TOP_LEFT,
                        duration=4000,    # won't disappear automatically
                        parent=self
                                        )
            return
        
        # Get the maximum and minimum values and smoothing parameters input by the user
        try:
            min_val = float(self.Passive_min.text()) if self.Passive_min.text() else None
            max_val = float(self.Passive_max.text()) if self.Passive_max.text() else None
            if min_val is not None and max_val is not None and min_val >= max_val:
                QMessageBox.warning(self, "Input error", "The minimum value must be less than the maximum value")
                return
            sigma = self.get_sigma_value()
        except ValueError:
            QMessageBox.warning(self, "Input error", "Please enter a valid number")
            return
        
        self.graphicsView_3.setStyleSheet("QGraphicsView { background-color: black; }")
        scene, data_min, data_max = self.load_raster(file_path, min_val, max_val, sigma)
        self.graphicsView_3.setScene(scene)
        self.Passive_min.setText(str(round(data_min, 3)))
        self.Passive_max.setText(str(round(data_max, 3)))
        self.graphicsView_3.fitInView(scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
        self.create_colorbar(
                min_val=float(self.Passive_min.text()),
                max_val=float(self.Passive_max.text()),
                cmap_name=self.cmap_combo.currentText(),
                target_widget=self.label_4)
    
    def render_Passive_max_pseudo_color(self, set_render_type=False):
        """Passive Max rendering"""
        if set_render_type:
            self.current_render_type = "PassiveMax"
        file_path = self.textBrowser_4.toPlainText()
        if not file_path:
            InfoBar.error(
                        title='Error!',
                        content="You have not selected a Passive Max file path!",
                        orient=Qt.Horizontal,
                        isClosable=True,
                        position=InfoBarPosition.TOP_LEFT,
                        duration=4000,    # won't disappear automatically
                        parent=self
                                        )
            return
        
        # Get the maximum and minimum values and smoothing parameters input by the user
        try:
            min_val = float(self.Passive_min_2.text()) if self.Passive_min_2.text() else None
            max_val = float(self.Passive_max_2.text()) if self.Passive_max_2.text() else None
            if min_val is not None and max_val is not None and min_val >= max_val:
                QMessageBox.warning(self, "Input error", "The minimum value must be less than the maximum value")
                return
            sigma = self.get_sigma_value()
        except ValueError:
            QMessageBox.warning(self, "Input error", "Please enter a valid number")
            return
        
        self.graphicsView_10.setStyleSheet("QGraphicsView { background-color: black; }")
        scene, data_min, data_max = self.load_raster(file_path, min_val, max_val, sigma)
        self.graphicsView_10.setScene(scene)
        self.Passive_min_2.setText(str(round(data_min, 3)))
        self.Passive_max_2.setText(str(round(data_max, 3)))
        self.graphicsView_10.fitInView(scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
        self.create_colorbar(
                min_val=float(self.Passive_min_2.text()),
                max_val=float(self.Passive_max_2.text()),
                cmap_name=self.cmap_combo.currentText(),
                target_widget=self.label_3
            )
    
    def display_sar_data(self):
        """Display SAR data"""
        filename, _ = QFileDialog.getOpenFileName(self, 'Open SAR data file', '', 'Raster files (*.tif *.jpg *.png);;All files (*)')
        if filename:
            self.textBrowser.setText(filename)
            QMessageBox.information(self, 'File path', f'Selected SAR file path: {filename}')
            file_path = self.textBrowser.toPlainText()
            self.graphicsView.setStyleSheet("QGraphicsView { background-color: black; }")
            sigma = self.get_sigma_value()
            scene, data_min, data_max = self.load_raster(file_path, sigma=sigma)
            self.graphicsView.setScene(scene)
            self.SAR_min.setText(str(round(data_min, 3)))
            self.SAR_max.setText(str(round(data_max, 3)))
            self.graphicsView.fitInView(scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

    # Core logic of pseudo-color rendering (with Gaussian smoothing)
    def load_raster(self, file_path, custom_min=None, custom_max=None, sigma=1.2):
        dataset = gdal.Open(file_path)
        if dataset is None:
            QMessageBox.information(self, 'Unable to open file', f'File path: {file_path}')
            return None, 0, 0

        band = dataset.GetRasterBand(1)
        data1 = band.ReadAsArray()
        print(f"Data shape: {data1.shape}, Data type: {data1.dtype}")
   
        # Process invalid values
        data1[data1 <= 0] = np.nan
        if np.all(np.isnan(data1)):
            QMessageBox.warning(self, "Data error", "All raster data is invalid")
            return None, 0, 0

        # Gaussian smoothing processing
        data_smoothed = np.copy(data1)
        data_smoothed[np.isnan(data_smoothed)] = 0  # Replace NaN with 0 for filtering
        data_smoothed = gaussian_filter(data_smoothed, sigma=sigma)  # Apply Gaussian filtering
        data_smoothed[np.isnan(data1)] = np.nan  # Restore NaN positions

        # Calculate statistical values
        valid_data = data_smoothed[~np.isnan(data_smoothed)]
        data_min, data_max = np.min(valid_data), np.max(valid_data)
        
        # Apply custom filtering range
        if custom_min is not None:
            valid_data = valid_data[valid_data >= custom_min]
        if custom_max is not None:
            valid_data = valid_data[valid_data <= custom_max]
        if len(valid_data) == 0:
            QMessageBox.warning(self, "Filtering result is empty", "No data meets the conditions, please adjust the filtering range")
            return None, data_min, data_max
        
        # Recalculate statistical values after filtering
        filtered_min, filtered_max = np.min(valid_data), np.max(valid_data)
        p1 = np.percentile(valid_data, 1)
        p99 = np.percentile(valid_data, 99)
        # Prioritize custom range, otherwise use percentile values
        norm = Normalize(
            vmin=custom_min if custom_min is not None else p1,
            vmax=custom_max if custom_max is not None else p99
        )

        # Apply pseudo-color
        cmap = plt.get_cmap(self.cmap_combo.currentText())
        sm = ScalarMappable(norm=norm, cmap=cmap)
        pseudo_color_data = sm.to_rgba(data_smoothed, bytes=True)
        
        # Process transparent areas
        alpha_channel = np.ones_like(data_smoothed, dtype=np.uint8) * 255
        alpha_channel[np.isnan(data_smoothed)] = 0
        # Set data outside the filtering range to transparent
        if custom_min is not None:
            alpha_channel[data_smoothed < custom_min] = 0
        if custom_max is not None:
            alpha_channel[data_smoothed > custom_max] = 0
        pseudo_color_data[:, :, 3] = alpha_channel
        pseudo_color_rgb = pseudo_color_data[:, :, :3].astype(np.uint8)
        pseudo_color_rgb = np.ascontiguousarray(pseudo_color_rgb)

        # Convert to QImage and display
        height, width = pseudo_color_rgb.shape[:2]
        image = QImage(pseudo_color_rgb.data, width, height, width*3, QImage.Format_RGB888)
        scene = QGraphicsScene()
        pixmap = QPixmap.fromImage(image)
        background = QPixmap(pixmap.size())
        background.fill(Qt.black)
        painter = QPainter(background)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()
        scene.addPixmap(background)

        return scene, filtered_min, filtered_max
    
    def set_zero_value_to_background(self, pixmap, background_color):
        image = pixmap.toImage()
        mask_color = image.pixelColor(0, 0).rgb()
        mask_image = image.createMaskFromColor(mask_color, Qt.MaskInColor)
        mask = QBitmap.fromImage(mask_image)
        pixmap.setMask(mask)
        background_image = QImage(pixmap.size(), QImage.Format_ARGB32)
        background_image.fill(background_color)
        painter = QPainter(background_image)
        painter.drawPixmap(QRect(0, 0, pixmap.width(), pixmap.height()), pixmap)
        painter.end()
        return QPixmap.fromImage(background_image)
    
    def wheelEvent(self, event: QWheelEvent):
        delta = event.angleDelta().y()
        pos = event.position().toPoint()
        if self.graphicsView.geometry().contains(pos):
            self.graphicsView.scale(1.15 if delta>0 else 1/1.15, 1.15 if delta>0 else 1/1.15)
        elif self.graphicsView_2.geometry().contains(pos):
            self.graphicsView_2.scale(1.15 if delta>0 else 1/1.15, 1.15 if delta>0 else 1/1.15)
        elif self.graphicsView_3.geometry().contains(pos):
            self.graphicsView_3.scale(1.15 if delta>0 else 1/1.15, 1.15 if delta>0 else 1/1.15)
        elif self.graphicsView_10.geometry().contains(pos):
            self.graphicsView_10.scale(1.15 if delta>0 else 1/1.15, 1.15 if delta>0 else 1/1.15)

class Retrieval(QWidget, Ui_retrieval):
    def __init__(self, controller, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.controller = controller
        self.controller.retrieval_window = self
        self.Out_path_select_4.clicked.connect(self.execute_output_path_set)
        self.Retrieval_button.clicked.connect(self.execute_retrieval)
        self.View_Soil_Moisture_button.clicked.connect(self.execute_button_open_file_SME)
        
        self.cmap_combo.setStyleSheet("""
            QComboBox {
            background-color: rgb(255, 255, 255);
            color:rgb(0,0,0);
            border: 1px solid #4a90e2;
            border-radius: 4px;
            padding: 2px 10px 2px 10px;
            }
            QComboBox QAbstractItemView {
            color:rgb(0,190,190); /* Dropdown list background color */
            background-color:rgb(255,255,255);     /* Dropdown list font color */           
            selection-background-color: #4a90e2;
            selection-color: #ffffff;
            }
        """)

        self.result_smooth_combo = QComboBox()
        self.result_smooth_combo.addItems(["Very low", "Low", "Medium", "High", "Very high", "Custom (0.1-5)"])
        self.result_smooth_combo.setStyleSheet("""
            QComboBox {
            background-color: rgb(255, 255, 255);
            color:rgb(0,0,0);
            border: 1px solid #4a90e2;
            border-radius: 4px;
            padding: 2px 10px 2px 10px;
            }
            QComboBox QAbstractItemView {
            color:rgb(0,190,190); /* Dropdown list background color */
            background-color:rgb(255,255,255);     /* Dropdown list font color */           
            selection-background-color: #4a90e2;
            selection-color: #ffffff;
            }
        """)
        self.result_smooth_combo.setCurrentText("Medium")
        self.horizontalLayout_4.addWidget(self.result_smooth_combo)
        self.result_sigma = QLineEdit("1.2")
        self.horizontalLayout_4.addWidget(self.result_sigma)

        # Connect signals to control the enable state of the input box
        self.result_smooth_combo.currentTextChanged.connect(self.update_result_sigma_enabled)
        self.update_result_sigma_enabled(self.result_smooth_combo.currentText())
        
        self.drag_data = {}
        self.draggable_views = [self.graphicsView_4]
        for view in self.draggable_views:
            self.drag_data[view] = {"start_pos": None, "is_dragging": False}
            view.viewport().installEventFilter(self)
            # Enable anti-aliasing and smooth scaling
            view.setRenderHint(QPainter.Antialiasing, True)
            view.setRenderHint(QPainter.SmoothPixmapTransform, True)
    
    def create_retrieval_colorbar(self, min_val, max_val, cmap_name):
        """Create a colorbar for the retrieval result (using the QLabel scheme)"""
        # Clear the original content
        for i in reversed(range(self.label_10.layout().count())) if self.label_10.layout() else []:
            self.label_10.layout().itemAt(i).widget().deleteLater()
    
        # Create a figure and axes
        fig = Figure(figsize=(3, 1))
        canvas = FigureCanvas(fig)
        ax = fig.add_axes([0, 0, 1, 1])  # Adjust the margins
    
        # Set the colormap
        cmap = plt.get_cmap(cmap_name)
        norm = Normalize(vmin=min_val, vmax=max_val)
    
        # Create a colorbar
        cb = fig.colorbar(
            ScalarMappable(norm=norm, cmap=cmap),
            cax=ax,
            orientation='horizontal'
        )   
        # Customize the appearance
        cb.ax.set_title('')
        cb.ax.tick_params(axis='both', which='both', length=0)
        cb.ax.set_xticks([])
        cb.ax.set_yticks([])
    
        # Set the QLabel layout
        if not self.label_10.layout():
            self.label_10.setLayout(QVBoxLayout())
            self.label_10.layout().setContentsMargins(0, 0, 0, 0)
    
        # Add the canvas to the QLabel
        self.label_10.layout().addWidget(canvas)
        canvas.draw()
    
        return canvas
    
    def update_result_sigma_enabled(self, text):
        """Enable or disable the result sigma input box according to the result smoothing level selection"""
        self.result_sigma.setEnabled(text == "Custom (0.1-5)")
        if text != "Custom (0.1-5)":
            if text == "Very low":
                self.result_sigma.setText("0.3")
            elif text == "Low":
                self.result_sigma.setText("0.8")
            elif text == "Medium":
                self.result_sigma.setText("1.2")
            elif text == "High":
                self.result_sigma.setText("2.0")
            elif text == "Very high":
                self.result_sigma.setText("3.5")
            self.result_sigma.setStyleSheet("background-color: #f0f0f0;")
        else:
            self.result_sigma.setStyleSheet("background-color: white;")
    
    def get_result_sigma_value(self):
        """Get the sigma value for result smoothing"""
        smooth_level = self.result_smooth_combo.currentText()
        if smooth_level == "Custom (0.1-5)":
            try:
                sigma = float(self.result_sigma.text())
                return sigma if 0.1 <= sigma <= 5 else 1.2
            except ValueError:
                return 1.2
        # Preset value mapping
        sigma_map = {
            "Very low": 0.3,
            "Low": 0.8,
            "Medium": 1.2,
            "High": 2.0,
            "Very high": 3.5
        }
        return sigma_map.get(smooth_level, 1.2)

    def execute_retrieval(self):
        """Execute soil moisture retrieval and display a "Please wait" pop-up window"""
        main_window = self.controller.main_window
    
        # Check the integrity of the input paths
        input_paths = [
            main_window.textBrowser.toPlainText(),    # SAR data
            main_window.textBrowser_2.toPlainText(),  # Passive Max
            main_window.textBrowser_4.toPlainText(),  # Passive Min
            main_window.textBrowser_3.toPlainText()   # SAR incidence angle
        ]
    
        if not all(input_paths) or not self.textBrowser_5.toPlainText():
            InfoBar.error(title="Path error", content="Please complete all input and output paths", parent=self)
            return

        # Create a "Please wait" pop-up window
        wait_dialog = QDialog(self)
        wait_dialog.setWindowTitle("Processing")
        wait_dialog.setFixedSize(400, 200)  # Fix the window size
        wait_dialog.setWindowModality(Qt.WindowModal)  # Modal window, prevent the user from operating other interfaces
    
        # Set the layout and prompt text
        layout = QVBoxLayout()
        label = QLabel("Soil moisture retrieval is in progress, please wait...")
        label.setAlignment(Qt.AlignCenter)  # Center the text
        label.setStyleSheet("font-size: 13px;")  # Adjust the font size
        layout.addWidget(label)
        wait_dialog.setLayout(layout)
    
    # Calculate centered position
        parent_geometry = self.geometry()
        dialog_geometry = wait_dialog.geometry()
        x = parent_geometry.x() + (parent_geometry.width() - dialog_geometry.width()) // 2
        y = parent_geometry.y() + (parent_geometry.height() - dialog_geometry.height()) // 2
        wait_dialog.move(x, y)

    # Display the dialog
        wait_dialog.show()
    
    # Force refresh the interface to ensure the dialog is displayed
        QApplication.processEvents()

        try:
        # Generate output filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            out_dir = self.textBrowser_5.toPlainText()
            out_path = f"{out_dir}/Soil_moisture_{timestamp}.tif"
        
        # Execute the inversion program (use subprocess to ensure blocking and wait for completion)
            result = subprocess.run(
                f'SM_Estimation_with_Psvbd_Main_pro.exe {input_paths[0]} {input_paths[1]} {input_paths[2]} {input_paths[3]} {out_path}',
                shell=True,
                check=True,
                capture_output=True,
                text=True
            )
        
        # Close the dialog
            wait_dialog.close()
        
            self.textBrowser_5.setPlainText(out_path)
            InfoBar.success(title="Inversion completed", content=f"Result saved to: {out_path}", parent=self)
        
        except subprocess.CalledProcessError as e:
            wait_dialog.close()
            InfoBar.error(title="Inversion failed", content=f"Program execution error: {e.stderr}", parent=self)
        except Exception as e:
            wait_dialog.close()
            InfoBar.error(title="Inversion failed", content=str(e), parent=self)
    
    def execute_output_path_set(self):
        directory = QFileDialog.getExistingDirectory(self, "Select folder", "/")
        if directory:
            self.textBrowser_5.setPlainText(directory)

    def execute_button_open_file_SME(self):
        file_path_Somoist = self.textBrowser_5.toPlainText()

        if not os.path.exists(file_path_Somoist):
            InfoBar.error(
                title='File does not exist',
                content=f"Path: {file_path_Somoist} is invalid",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP_LEFT,
                duration=3000,
                parent=self
            )
            return
        
        # Read the maximum and minimum values input on the interface for filtering
        try:
            min_val = float(self.SME_min.text()) if self.SME_min.text().strip() else None
            max_val = float(self.SME_max.text()) if self.SME_max.text().strip() else None
            
            # Verify that the minimum value cannot be greater than the maximum value
            if min_val is not None and max_val is not None and min_val >= max_val:
                QMessageBox.warning(self, "Input error", "Minimum value must be less than maximum value")
                return
        except ValueError as e:
            QMessageBox.warning(self, "Input error", f"Please enter valid numbers: {str(e)}")
            return
        
        sigma = self.get_result_sigma_value()
        self.graphicsView_4.setStyleSheet("QGraphicsView { background-color: black; }")
        # Pass the filtered maximum and minimum values when calling load_raster
        scene_4, data_min, data_max = self.load_raster(file_path_Somoist, sigma, min_val, max_val)  
        if scene_4 is not None:
            self.graphicsView_4.setScene(scene_4)
            # Fill the actual maximum and minimum values of the filtered data back to the interface controls
            self.SME_min.setText(str(round(data_min, 3)))  
            self.SME_max.setText(str(round(data_max, 3)))  
            self.graphicsView_4.fitInView(scene_4.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
            self.create_retrieval_colorbar(
            min_val=float(self.SME_min.text()),
            max_val=float(self.SME_max.text()),
            cmap_name=self.cmap_combo.currentText()
            )
        else:
            InfoBar.error(
                title='Rendering failed',
                content="No valid scene generated, cannot render",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=3000,
                parent=self
            )


    def load_raster(self, file_path, sigma=1.2, custom_min=None, custom_max=None):
        dataset = gdal.Open(file_path)
        if dataset is None:
            QMessageBox.information(self, 'Cannot open file', f'File path: {file_path}')
            return None, 0, 0

        band = dataset.GetRasterBand(1)
        data1 = band.ReadAsArray()
        data1[data1 <= 0] = np.nan
        
        # Gaussian smoothing processing
        data_smoothed = np.copy(data1)
        data_smoothed[np.isnan(data_smoothed)] = 0
        data_smoothed = gaussian_filter(data_smoothed, sigma=sigma)
        data_smoothed[np.isnan(data1)] = np.nan

        if np.all(np.isnan(data_smoothed)):
            QMessageBox.warning(self, "Data error", "All raster data values are invalid")
            return None, 0, 0

        valid_data = data_smoothed[~np.isnan(data_smoothed)]
        # Apply custom maximum and minimum value filtering
        if custom_min is not None:
            valid_data = valid_data[valid_data >= custom_min]
        if custom_max is not None:
            valid_data = valid_data[valid_data <= custom_max]
        if len(valid_data) == 0:
            QMessageBox.warning(self, "Filter result is empty", "No data meets the conditions, please adjust the filtering range")
            return None, np.nanmin(data_smoothed), np.nanmax(data_smoothed)
        
        data_min, data_max = np.min(valid_data), np.max(valid_data)
        p1 = np.percentile(valid_data, 1) if len(valid_data) > 0 else np.nanmin(data_smoothed)
        p99 = np.percentile(valid_data, 99) if len(valid_data) > 0 else np.nanmax(data_smoothed)
        
        # Priority is given to the passed custom range; otherwise, use percentile values
        norm = Normalize(
            vmin=custom_min if custom_min is not None else p1,
            vmax=custom_max if custom_max is not None else p99
        )

        cmap = plt.get_cmap(self.cmap_combo.currentText())
        sm = ScalarMappable(norm=norm, cmap=cmap)
        pseudo_color_data = sm.to_rgba(data_smoothed, bytes=True)
        
        alpha_channel = np.ones_like(data_smoothed, dtype=np.uint8) * 255
        alpha_channel[np.isnan(data_smoothed)] = 0
        # Set transparent areas according to filtering conditions
        if custom_min is not None:
            alpha_channel[data_smoothed < custom_min] = 0
        if custom_max is not None:
            alpha_channel[data_smoothed > custom_max] = 0
        pseudo_color_data[:, :, 3] = alpha_channel
        pseudo_color_rgb = pseudo_color_data[:, :, :3].astype(np.uint8)
        pseudo_color_rgb = np.ascontiguousarray(pseudo_color_rgb)

        height, width = pseudo_color_rgb.shape[:2]
        image = QImage(pseudo_color_rgb.data, width, height, width*3, QImage.Format_RGB888)
        scene = QGraphicsScene()
        pixmap = QPixmap.fromImage(image)
        background = QPixmap(pixmap.size())
        background.fill(Qt.black)
        painter = QPainter(background)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()
        scene.addPixmap(background)

        return scene, data_min, data_max
    
    def set_zero_value_to_background(self, pixmap, background_color):
        image = pixmap.toImage()
        mask_color = image.pixelColor(0, 0).rgb()
        mask_image = image.createMaskFromColor(mask_color, Qt.MaskInColor)
        mask = QBitmap.fromImage(mask_image)
        pixmap.setMask(mask)
        background_image = QImage(pixmap.size(), QImage.Format_ARGB32)
        background_image.fill(background_color)
        painter = QPainter(background_image)
        painter.drawPixmap(QRect(0, 0, pixmap.width(), pixmap.height()), pixmap)
        painter.end()
        return QPixmap.fromImage(background_image)
    
    def wheelEvent(self, event: QWheelEvent):
        delta = event.angleDelta().y()
        pos = event.position().toPoint()
        if self.graphicsView_4.geometry().contains(pos):
            self.graphicsView_4.scale(1.15 if delta>0 else 1/1.15, 1.15 if delta>0 else 1/1.15)
    
    def eventFilter(self, source: QObject, event: QEvent) -> bool:
        view_map = {view.viewport(): view for view in self.draggable_views}
        view = view_map.get(source)
        
        if view is None:
            return super().eventFilter(source, event)
        
        if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
            self.drag_data[view]["start_pos"] = event.pos()
            self.drag_data[view]["is_dragging"] = True
            view.setCursor(Qt.ClosedHandCursor)
            return True
        
        elif event.type() == QEvent.MouseMove:
            if self.drag_data[view]["is_dragging"] and self.drag_data[view]["start_pos"]:
                delta = event.pos() - self.drag_data[view]["start_pos"]
                self.drag_data[view]["start_pos"] = event.pos()
                h_bar = view.horizontalScrollBar()
                v_bar = view.verticalScrollBar()
                h_bar.setValue(h_bar.value() - delta.x())
                v_bar.setValue(v_bar.value() - delta.y())
                return True
        
        elif event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
            self.drag_data[view]["is_dragging"] = False
            self.drag_data[view]["start_pos"] = None
            view.setCursor(Qt.ArrowCursor)
            return True
        
        return super().eventFilter(source, event)

class Module3(QWidget, Ui_TimeSeries):
    def __init__(self, controller, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.controller = controller
        self.Out_path_select_6.clicked.connect(self.select_tif_file)
        self.TimeSeries_2.clicked.connect(self.analyze_time_series)

        # Bind button functions
        self.pushButton_TSA.clicked.connect(self.save_images_to_folder)  # Save images to folder
        self.pushButton_csv.clicked.connect(self.save_data_to_csv)      # Save CSV file
        
        # Initialize variables to store analysis data
        self.data_series = None
        self.band_images = None

    def select_tif_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select multi-band image file", "", "TIF files (*.tif *.tiff);;All files (*)")
        if file_path:
            self.textBrowser_t.setText(file_path)

    def analyze_time_series(self):
        tif_path = self.textBrowser_t.toPlainText()
        if not os.path.exists(tif_path):
            #QMessageBox.warning(self, "Path error", "Please select a valid multi-band TIF file path")
            InfoBar.error(
                title='Path error',
                content="Please select a valid multi-band TIF file path",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=3000,
                parent=self
            )
            return

        try:
            dataset = gdal.Open(tif_path)
            if dataset is None:
                raise RuntimeError("Cannot read TIF file")
            band_count = dataset.RasterCount
            print(f"Detected {band_count} bands in total")

            self.data_series = []
            self.band_images = []

            for i in range(1, band_count + 1):
                band = dataset.GetRasterBand(i)
                data = band.ReadAsArray().astype(np.float32)
                data[data <= 0] = np.nan
                band_mean = np.nanmean(data)
                self.data_series.append(band_mean)
                self.band_images.append(data)
                print(f"Band {i} mean value: {band_mean}")

            # Display the chart in the interface
            self.plot_series_to_view(self.data_series)

        except Exception as e:
            QMessageBox.critical(self, "Analysis error", f"Error occurred while processing time series analysis: {str(e)}")
    def eventFilter(self, obj, event):
        """Handle mouse wheel events for the canvas"""
        # Only intercept wheel events, not mouse press/move events
        if isinstance(obj, FigureCanvas) and event.type() == QEvent.Type.Wheel:
            scale_factor = 1.15 if event.angleDelta().y() > 0 else 0.85
            self.graphicsView_6.scale(scale_factor, scale_factor)
            return True  # Intercept wheel events
        return super().eventFilter(obj, event)  # Pass other events normally
    def wheelEvent(self, event):
        """Handle mouse wheel events for blank areas"""
        if self.graphicsView_6.underMouse():
            scale_factor = 1.15 if event.angleDelta().y() > 0 else 0.85
            self.graphicsView_6.scale(scale_factor, scale_factor)
            event.accept()
        else:
            super().wheelEvent(event)
    def plot_series_to_view(self, data_series):
        """Embed the line chart into graphicsView_6, supporting zoom and pan"""
        fig = Figure(figsize=(7, 4))
        ax = fig.add_subplot(111)
        ax.plot(range(1, len(data_series) + 1), data_series, marker='o')
        ax.set_title("Time series average analysis")
        ax.set_xlabel("Band number")
        ax.set_ylabel("Average value")
        ax.grid(True)

    # Create a completely passive canvas (does not intercept any events)
        class PassiveCanvas(FigureCanvas):
            def __init__(self, figure):
                super().__init__(figure)
                self.setFocusPolicy(Qt.NoFocus)  # Do not receive focus
                self.setAttribute(Qt.WA_TransparentForMouseEvents, True)  # Mouse events pass through

        # Disable all functions that may intercept events
            def mousePressEvent(self, event): event.ignore()
            def mouseMoveEvent(self, event): event.ignore()
            def mouseReleaseEvent(self, event): event.ignore()
            def wheelEvent(self, event): event.ignore()

        canvas = PassiveCanvas(fig)
    
    # Disable Matplotlib default interaction
        fig.canvas.mpl_connect('scroll_event', lambda event: None)
        fig.set_tight_layout(True)
    
    # Configure graphicsView_6
        if not self.graphicsView_6.scene():
            self.graphicsView_6.setScene(QGraphicsScene())
        else:
            self.graphicsView_6.scene().clear()
    
        self.graphicsView_6.scene().addWidget(canvas)
        self.graphicsView_6.scene().setSceneRect(canvas.rect())
    
    # View configuration - enable dragging and zooming
        self.graphicsView_6.setRenderHint(QPainter.Antialiasing)
        self.graphicsView_6.setDragMode(QGraphicsView.ScrollHandDrag)  # Enable dragging
        self.graphicsView_6.setInteractive(True)  # Enable interaction
        self.graphicsView_6.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.graphicsView_6.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.graphicsView_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView_6.fitInView(self.graphicsView_6.sceneRect(), Qt.KeepAspectRatio)

    # Handle wheel zoom directly on graphicsView_6
        def handle_wheel_event(event):
            scale_factor = 1.15 if event.angleDelta().y() > 0 else 0.85
            self.graphicsView_6.scale(scale_factor, scale_factor)
            event.accept()

        self.graphicsView_6.wheelEvent = handle_wheel_event
    def show_each_band_image(self, band_data_list):
        for idx, band_data in enumerate(band_data_list):
            fig, ax = plt.subplots()
            cax = ax.imshow(band_data, cmap='jet')
            ax.set_title(f"Band {idx + 1} image")
            plt.colorbar(cax)
            plt.tight_layout()

    def save_images_to_folder(self):
        """Save all band images to the selected folder"""
        if not self.band_images:
            InfoBar.error(
                title='Warning',
                content="Please perform time series analysis first to generate image data",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=3000,
                parent=self
            )
            return
            
        # Open folder selection dialog
        folder = QFileDialog.getExistingDirectory(self, "Select folder to save images", "")
        if not folder:
            return
            
        # Save images of each band
        for idx, image_data in enumerate(self.band_images):
            try:
                fig, ax = plt.subplots()
                cax = ax.imshow(image_data, cmap='jet')
                ax.set_title(f"Band {idx + 1} image")
                plt.colorbar(cax)
                plt.tight_layout()
                
                # Save image to selected folder
                image_path = os.path.join(folder, f"band_{idx + 1}_image.png")
                plt.savefig(image_path, dpi=300, bbox_inches='tight')
                plt.close(fig)
                
            except Exception as e:
                InfoBar.error(
                    title='Saving failed',
                    content=f"Error saving image for band {idx + 1}: {str(e)}",
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP,
                    duration=3000,
                    parent=self
                )
        
        InfoBar.success(
            title='Saving successful',
            content=f"All images saved to: {folder}",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=3000,
            parent=self
        )

    def save_data_to_csv(self):
        """Save average value data as a CSV file"""
        if not self.data_series:
            InfoBar.error(
                title='Warning',
                content="Please perform time series analysis first to generate data",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=3000,
                parent=self
            )
            return
            
        # Open file save dialog
        save_path, _ = QFileDialog.getSaveFileName(self, "Save CSV file", "", "CSV Files (*.csv)")
        if not save_path:
            return
            
        try:
            with open(save_path, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["Band", "MeanValue"])  # Write header
                for i, value in enumerate(self.data_series, start=1):
                    writer.writerow([f"Band_{i}", round(value, 6)])  # Keep 6 decimal places
            
            InfoBar.success(
                title='Saving successful',
                content=f"CSV file saved to: {save_path}",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=3000,
                parent=self
            )
            
        except Exception as e:
            InfoBar.error(
                title='Saving failed',
                content=f"Error saving CSV file: {str(e)}",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=3000,
                parent=self
            )

class navigation(SplitFluentWindow):
    def __init__(self):
        super().__init__()
        self.controller = AppController()
        self.main_widget = Mainwindow(self.controller)
        self.addSubInterface(self.main_widget, FluentIcon.SEND, 'Input Data')
        self.retrieval_widget = Retrieval(self.controller)
        self.addSubInterface(self.retrieval_widget, FluentIcon.PLAY, 'Soil Moisture Estimation	')
        self.module3_widget = Module3(self.controller)
        self.addSubInterface(self.module3_widget, FluentIcon.ACCEPT, 'Time Series Analysis')  # Use time series icon

        QTimer.singleShot(10, self.center_window)
    def center_window(self):
        # Get the screen where the current window is located
        screen = self.screen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.geometry()
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        self.move(x, y)

if __name__ == "__main__":
    app = QApplication([])
    window = login()
    window.show()
    app.exec()