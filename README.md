# Alternovation Project

## Overview
The Alternovation project, developed at Ural Federal University in Russia, introduces an innovative Python-based application that automates the visualization and cost estimation of furniture based on user-defined specifications. Utilizing cutting-edge machine learning algorithms and a user-friendly interface, this project aims to revolutionize the way we design and budget for furniture.

## Features
1. **Furniture Visualization:** Generates high-quality images of furniture based on user inputs such as         type, purpose, texture, and dimensions.
2. **Cost Estimation:** Employs a pre-trained CatBoostRegressor model to provide an accurate estimate of the     furniture's manufacturing cost.
3. **Interactive UI:** Built with Gradio, offering a seamless and interactive experience for users to input     their specifications and view the generated furniture images along with cost estimations.
4. **API Integration:** Utilizes external APIs for dynamic furniture image generation.

## Technologies Used
1. **Python:** The core programming language of the project.
2. **Gradio:** For creating the interactive web interface.
3. **CatBoostRegressor:** For machine learning-based cost estimation.
4. **Requests, Pillow, Numpy, Joblib, Scikit-learn:** For various data processing and machine learning tasks.
5. **HTML/CSS:** For frontend design and interaction.

## Getting Started
_Prerequisites_
Ensure you have Python 3.6+ installed on your system. Additionally, you will need pip for installing Python packages.

## Installation
**Clone the Repository**

    git clone https://github.com/ChinmayBitne/alternovation-project.git

    cd alternovation-project

_Set Up a Virtual Environment (Optional but recommended)_

For Windows:
   
    python -m venv venv

    venv\Scripts\activate
    
For macOS and Linux:
    
    python3 -m venv venv

    source venv/bin/activate
    
**Install Dependencies**

     pip install -r requirements.txt
     
## Usage
Start the Application

Run the following command in your terminal:

     python app.py
     
Access the Web Interface

Open a web browser and navigate to the URL indicated in your terminal (typically http://127.0.0.1:7860).

*Generate Furniture and Estimate Cost*

1. Input your furniture specifications using the web interface.
2. Click on the "Generate" button to view the furniture image and cost estimation.


## Acknowledgments
Ural Federal University, for providing the platform and support for this innovative project.
