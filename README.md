# Medical Data Visualizer

This project visualizes medical examination data using Python, Pandas, Seaborn, and Matplotlib. The goal is to explore relationships between cardiovascular disease, body measurements, blood markers, and lifestyle factors.

---

## Dataset

- **File:** `medical_examination.csv`
- **Description:** Each row represents a patient and columns contain features such as age, height, weight, blood pressure, cholesterol, glucose, lifestyle habits, and cardiovascular disease indicator.
- **Source:** freeCodeCamp Medical Data Visualizer Project

| Feature | Type | Description |
|---------|------|-------------|
| age | int | Age in days |
| height | int | Height in cm |
| weight | float | Weight in kg |
| gender | categorical | Gender code |
| ap_hi | int | Systolic blood pressure |
| ap_lo | int | Diastolic blood pressure |
| cholesterol | int | 1: normal, 2: above normal, 3: well above normal |
| gluc | int | 1: normal, 2: above normal, 3: well above normal |
| smoke | binary | Smoking status |
| alco | binary | Alcohol intake |
| active | binary | Physical activity |
| cardio | binary | Presence of cardiovascular disease (target) |

---

## Features

1. **Overweight column**: Added using BMI calculation. `1` = overweight, `0` = not overweight.  
2. **Normalized cholesterol & glucose**: Values are converted to `0` = good, `1` = bad.  
3. **Categorical plot**: Counts of cholesterol, glucose, smoke, alcohol, activity, and overweight split by cardiovascular disease.  
4. **Heatmap**: Correlation matrix of cleaned dataset (removing outliers and invalid values).  

---


---

## Installation

1. Clone the repository:
   ```bash
   git clone <your-github-url>
   cd medical-visualizer
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\Activate.bin
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the script to generate plots:
   ```bash
   python main.py
5. Optional: Run unit tests
    ```bash
   pytest -q

