# SAR-SoMoist V1.0  
**A High-Resolution Soil Moisture Retrieval and Mapping Software with SAR and Passive Microwave Remote Sensing Datasets**  

## Introduction  
SAR-SoMoist is an integrated software tool for high-resolution soil moisture retrieval and mapping, utilizing both **Synthetic Aperture Radar (SAR)** and **passive microwave remote sensing datasets**. It provides a user-friendly graphical interface for:  
- Data import  
- Pseudo-color rendering  
- Soil moisture inversion  
- Time series analysis  
- Result export  

Designed for **research, agriculture, and environmental monitoring** applications.

## Development Team
- **Developer**: Shi,Hongtao and Wu,Qing and Wang,Yijia and Cao,Jiaxin and He,Ruirui and Wang Yangguang.
- **Affiliation**: China University of Mining and Technology,School of Environment and Spatial Informatics.
- **Contact Email**: hongtao.shi@cumt.edu.cn

## Features  
- **Multi-source data support**: Import SAR and passive microwave remote sensing images.  
- **Visualization**: Pseudo-color rendering and interactive mapping.  
- **High-resolution retrieval**: Accurate soil moisture estimation at fine spatial scales.  
- **Time series analysis**: Plot mean values and track temporal trends.  
- **Export flexibility**: Save results as images (PNG/JPG) or CSV files.  
- **Customizable GUI**: Adjust parameters via an intuitive interface.  

## Installation & Usage  
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yijiawang111/SAR_Soil_Moisture_Estimation-SAR_SoMoist
   cd SAR_Soil_Moisture_Estimation-SAR_SoMoist
   ```
2. **Set up a Python virtual environment (recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   Ensure you have Python 3.8 or newer. Then install the required packages using pip:
   ```bash
   pip install PySide6 GDAL matplotlib scipy qfluentwidgets
   ```
