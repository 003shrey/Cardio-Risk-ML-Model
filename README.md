# ❤️ Cardio-Risk-ML-Model

A Machine Learning-powered web application that predicts the risk of heart disease based on various clinical and physiological parameters. This project leverages the K-Nearest Neighbors (KNN) algorithm to analyze patient data and provide real-time risk assessments.

## 🌐 Live Demo

**Try the application here:** [Cardio Risk ML Model](https://cardio-risk-ml-model-9yeiftolaxgimwcls4duzm.streamlit.app/)

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Dataset Information](#dataset-information)
- [Model Details](#model-details)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Key Insights](#key-insights)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## 🎯 About the Project

Heart disease remains one of the leading causes of mortality worldwide. This project aims to provide an accessible, user-friendly tool for preliminary heart disease risk assessment. By analyzing key health indicators such as age, blood pressure, cholesterol levels, and exercise-induced symptoms, the model helps identify individuals who may be at higher risk and should seek professional medical consultation.

The application uses a trained K-Nearest Neighbors (KNN) machine learning model that has been optimized for accuracy and deployed as an interactive web interface using Streamlit.

## ✨ Features

- **Interactive User Interface**: Easy-to-use web interface built with Streamlit
- **Real-time Predictions**: Instant risk assessment based on input parameters
- **Probability Scores**: Displays the calculated probability percentage of heart disease risk
- **Multiple Input Parameters**: Considers 11 different clinical features including:
  - Age
  - Sex
  - Chest Pain Type (Asymptomatic, Atypical Angina, Non-Anginal Pain, Typical Angina)
  - Resting Blood Pressure
  - Cholesterol Levels
  - Fasting Blood Sugar
  - Resting ECG Results
  - Maximum Heart Rate
  - Exercise-Induced Angina
  - ST Depression (Oldpeak)
  - ST Slope
- **Visual Risk Indicators**: Color-coded results (Green for low risk, Red for high risk)
- **Scalable and Deployable**: Ready for cloud deployment on Streamlit Cloud

## 📊 Dataset Information

The model is trained on a comprehensive heart disease dataset containing **918 patient records** with the following characteristics:

- **Source**: Kaggle Heart Disease Dataset
- **Features**: 11 clinical and demographic features
- **Target Variable**: Binary classification (Heart Disease: Yes/No)
- **Feature Types**:
  - **Numerical Features**: Age, RestingBP, Cholesterol, MaxHR, Oldpeak
  - **Categorical Features**: Sex, ChestPainType, RestingECG, ExerciseAngina, ST_Slope, FastingBS

### Feature Descriptions

| Feature | Description | Values/Range |
|---------|-------------|--------------|
| Age | Patient's age in years | 18-100 years |
| Sex | Patient's biological sex | Male/Female |
| ChestPainType | Type of chest pain experienced | ATA (Atypical Angina), NAP (Non-Anginal Pain), ASY (Asymptomatic), TA (Typical Angina) |
| RestingBP | Resting blood pressure | 80-200 mm Hg |
| Cholesterol | Serum cholesterol level | 100-600 mg/dL |
| FastingBS | Fasting blood sugar > 120 mg/dL | 0 (No), 1 (Yes) |
| RestingECG | Resting electrocardiogram results | Normal, ST (ST-T wave abnormality), LVH (Left Ventricular Hypertrophy) |
| MaxHR | Maximum heart rate achieved | 60-220 bpm |
| ExerciseAngina | Exercise-induced angina | Y (Yes), N (No) |
| Oldpeak | ST depression induced by exercise | 0.0-6.0 |
| ST_Slope | Slope of peak exercise ST segment | Up, Flat, Down |

## 🤖 Model Details

### Algorithm: K-Nearest Neighbors (KNN)

The project uses the **K-Nearest Neighbors** algorithm, a non-parametric supervised learning method used for classification. The model works by:

1. **Data Preprocessing**:
   - One-hot encoding for categorical variables
   - Feature scaling using StandardScaler
   - Missing value handling

2. **Model Training**:
   - Algorithm: KNN Classifier
   - Features: 11 clinical parameters (expanded to multiple features after encoding)
   - Target: Binary classification (Heart Disease presence)

3. **Prediction Process**:
   - Accepts user input through the Streamlit interface
   - Encodes categorical features using one-hot encoding
   - Scales numerical features using the pre-trained scaler
   - Makes predictions using the trained KNN model
   - Outputs both binary prediction and probability score

### Model Performance

The model has been trained and validated to provide reliable predictions. Key observations include:

- **Risk probability increases significantly when exercise-induced angina is present**, reflecting known clinical patterns
- The model performs well on borderline cases, providing nuanced probability scores
- Regular validation ensures consistent performance across different patient profiles

## 🛠️ Technologies Used

### Machine Learning & Data Science
- **Python 3.x**: Core programming language
- **scikit-learn**: Machine learning library for KNN model
- **NumPy**: Numerical computing
- **Pandas**: Data manipulation and analysis
- **Joblib**: Model serialization and deserialization

### Data Visualization & Analysis
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical data visualization
- **Jupyter Notebook**: Exploratory data analysis and model development

### Web Application
- **Streamlit**: Web application framework for creating the interactive UI

### Deployment
- **Streamlit Cloud**: Cloud hosting platform for deployment

## 📥 Installation

Follow these steps to run the application locally:

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step-by-Step Setup

1. **Clone the repository**
```bash
git clone https://github.com/003shrey/Cardio-Risk-ML-Model.git
cd Cardio-Risk-ML-Model
```

2. **Create a virtual environment (recommended)**
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install required dependencies**
```bash
pip install -r requirements.txt
```

4. **Verify model files are present**
Ensure the following files exist in the project directory:
- `knn_heart_model.pkl` (trained KNN model)
- `scaler.pkl` (feature scaler)
- `columns.pkl` (expected feature columns)

5. **Run the Streamlit application**
```bash
streamlit run app.py
```

6. **Access the application**
Open your web browser and navigate to:
```
http://localhost:8501
```

## 🚀 Usage

### Using the Web Application

1. **Access the Application**: Open the [live deployment link](https://cardio-risk-ml-model-9yeiftolaxgimwcls4duzm.streamlit.app/) or run it locally

2. **Enter Patient Information**:
   - Adjust the **Age** slider (18-100 years)
   - Select **Sex** (Male/Female)
   - Choose **Chest Pain Type** from the dropdown
   - Input **Resting Blood Pressure** (mm Hg)
   - Enter **Cholesterol** level (mg/dL)
   - Indicate if **Fasting Blood Sugar** > 120 mg/dL
   - Select **Resting ECG** results
   - Set **Maximum Heart Rate** achieved
   - Indicate **Exercise-Induced Angina** (Yes/No)
   - Adjust **Oldpeak** slider for ST depression
   - Select **ST Slope** type

3. **Get Prediction**:
   - Click the **"Predict"** button
   - View the **risk probability percentage**
   - See the **color-coded result**:
     - 🟢 **Green (Success)**: Low Risk of Heart Disease
     - 🔴 **Red (Error)**: High Risk of Heart Disease

4. **Interpret Results**:
   - The probability score indicates the likelihood of heart disease
   - Higher percentages indicate higher risk
   - Results are for preliminary assessment only
   - **Always consult a healthcare professional for medical advice**

### Example Use Case

**Scenario**: A 55-year-old male with chest pain wants to assess his heart disease risk.

**Input Parameters**:
- Age: 55
- Sex: Male
- Chest Pain Type: Atypical Angina (ATA)
- Resting BP: 140 mm Hg
- Cholesterol: 250 mg/dL
- Fasting BS: Yes (1)
- Resting ECG: Normal
- Max HR: 150 bpm
- Exercise Angina: Yes
- Oldpeak: 2.0
- ST Slope: Flat

**Output**: The model will calculate the risk probability and display whether the patient is at low or high risk for heart disease.

## 📁 Project Structure

```
Cardio-Risk-ML-Model/
│
├── app.py                      # Main Streamlit application
├── heart_model.ipynb           # Jupyter notebook for model training and EDA
├── knn_heart_model.pkl         # Trained KNN model (serialized)
├── scaler.pkl                  # Feature scaler (serialized)
├── columns.pkl                 # Expected feature columns (serialized)
├── heart.csv                   # Heart disease dataset
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation (this file)
├── change_log.md              # Project development changelog
├── LICENSE                     # MIT License
└── .devcontainer/             # Development container configuration
    └── devcontainer.json
```

### Key Files Description

- **app.py**: Contains the Streamlit web application code with user interface and prediction logic
- **heart_model.ipynb**: Jupyter notebook with exploratory data analysis, feature engineering, model training, and evaluation
- **knn_heart_model.pkl**: Serialized KNN model ready for predictions
- **scaler.pkl**: StandardScaler object used to normalize input features
- **columns.pkl**: List of expected feature columns after encoding
- **heart.csv**: Original dataset with 918 patient records
- **requirements.txt**: All Python package dependencies needed to run the project

## 💡 Key Insights

Based on the model training and analysis, several important insights have been discovered:

1. **Exercise-Induced Angina**: Risk probability increases significantly when exercise-induced angina is present, reflecting well-known clinical patterns in cardiology

2. **Chest Pain Type**: Asymptomatic chest pain (ASY) often correlates with higher risk, highlighting the importance of subtle symptoms

3. **ST Slope**: The slope of the peak exercise ST segment is a strong predictor, with flat or downward slopes indicating higher risk

4. **Age and Max Heart Rate**: Combined analysis of age with maximum heart rate achieved provides valuable risk stratification

5. **Multiple Risk Factors**: The model considers the interaction of multiple features, providing more nuanced predictions than single-factor analysis

## 🔮 Future Enhancements

Planned improvements and features for future versions:

- [ ] **Additional ML Models**: Implement and compare Random Forest, XGBoost, and Neural Networks
- [ ] **Model Performance Metrics**: Display accuracy, precision, recall, and F1-score on the UI
- [ ] **Feature Importance Visualization**: Show which features contribute most to the prediction
- [ ] **Historical Data Tracking**: Allow users to save and track predictions over time
- [ ] **PDF Report Generation**: Generate downloadable medical reports with predictions
- [ ] **Multi-language Support**: Add support for multiple languages
- [ ] **Mobile App Version**: Develop iOS and Android applications
- [ ] **Doctor Dashboard**: Create a separate interface for healthcare providers to review multiple patient assessments
- [ ] **Integration with EHR Systems**: Connect with Electronic Health Record systems for seamless data flow
- [ ] **Real-time Model Retraining**: Implement continuous learning with new validated data

## 🤝 Contributing

Contributions are welcome and greatly appreciated! If you have suggestions for improvements, please follow these steps:

1. **Fork the Project**
2. **Create your Feature Branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your Changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the Branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Contribution Guidelines

- Ensure your code follows PEP 8 style guidelines
- Add comments and documentation for new features
- Test your changes thoroughly before submitting
- Update the README.md if you add new features
- Be respectful and constructive in discussions

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2025 Shreyansh Yadav

## 👨‍💻 Author

**Shreyansh Yadav**

- GitHub: [@003shrey](https://github.com/003shrey)
- Project Link: [https://github.com/003shrey/Cardio-Risk-ML-Model](https://github.com/003shrey/Cardio-Risk-ML-Model)
- Live Application: [Cardio Risk ML Model](https://cardio-risk-ml-model-9yeiftolaxgimwcls4duzm.streamlit.app/)

## ⚠️ Disclaimer

**Important Medical Disclaimer**:

This application is designed for educational and informational purposes only. It is NOT intended to be a substitute for professional medical advice, diagnosis, or treatment. 

- Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition
- Never disregard professional medical advice or delay in seeking it because of something you have read or results generated by this application
- If you think you may have a medical emergency, call your doctor or emergency services immediately
- The predictions made by this model are based on statistical patterns and should not be considered as definitive medical diagnoses

## 🙏 Acknowledgments

- Dataset source: Kaggle Heart Disease Dataset
- Streamlit team for the amazing framework
- The open-source community for various libraries and tools
- Healthcare professionals whose research made this project possible

---

**⭐ If you find this project helpful, please consider giving it a star!**

---

*Last Updated: December 2025*
