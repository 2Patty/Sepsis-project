Sepsis Prediction Project

Objective

The primary goal of this project is to predict the likelihood of a patient developing sepsis based on clinical and demographic data. The insights from this analysis aim to:
Improve early detection of sepsis in hospitals or clinics.
Optimize resource allocation for high-risk patients.
Reduce sepsis-related mortality rates by facilitating timely intervention.

Project Overview:

i. Data Collection and Preprocessing
I gathered and prepared a comprehensive dataset containing clinical and physiological information about patients. This data was preprocessed to ensure it was suitable for training and evaluating the sepsis classification model.

ii. Machine Learning Model
A machine learning model specifically designed for sepsis classification was developed and fine-tuned. The model achieves high accuracy, enabling early detection of sepsis, which is critical for prompt medical intervention.

iii. FastAPI Integration
The trained machine learning model was integrated into an API using FastAPI. This API enables healthcare professionals to input patient information and receive immediate predictions regarding the risk of sepsis.

iv. Docker Deployment
The entire application was containerized and deployed using Docker, ensuring smooth and consistent performance across different environments.


Project Setup

Follow these steps to configure the project environment:

i. Clone the Repository
Run the following command to clone the project repository:

bash
Copy code
git clone (https://github.com/2Patty/Sepsis-project.git)

ii. Set Up a Virtual Environment and Install Dependencies

For Windows:

Create and activate a virtual environment:
bash
Copy code
python -m venv venv
venv\Scripts\activate

Upgrade pip and install the required dependencies:
bash
Copy code
python -m pip install -q --upgrade pip
python -m pip install -qr requirements.txt
You can copy and execute each of the commands above in your terminal to quickly prepare the project environment.


columns in the data

ID: number to represent patient ID

PRG: Plasma glucose

PL: Blood Work Result-1 (mu U/ml)

PR: Blood Pressure (mm Hg)

SK: Blood Work Result-2 (mm)

TS: Blood Work Result-3 (mu U/ml)

M11: Body mass index (weight in kg/(height in m)^2

BD2: Blood Work Result-4 (mu U/ml)

Age: patients age (years)

Insurance: If a patient holds a valid insurance card

Sepsis: Positive: if a patient in ICU will develop sepsis and Negative: otherwise

Steps Followed
1. Data Exploration
Understanding the dataset structure, identifying missing values, and analyzing data types.
Descriptive statistics to summarize numerical variables.

2. Data Cleaning
Handling missing values and duplicates.

3. Exploratory Data Analysis (EDA)
Univariate Analysis: Examining individual variables.
Bivariate Analysis: Analyzing relationships between variables.
Correlation Analysis: Identifying significant relationships among numerical features.

4. Data Preparation
Feature engineering and balancing the dataset to handle class imbalance.

5. Modeling and Evaluation
Building and evaluating machine learning models to predict sepsis risk.
Hyperparameter tuning for model optimization.
I was testing the best model on the test set.

6. Insights and Conclusion
Summarizing the results and highlighting actionable insights.

Deployment

i. FastAPI
The model is implemented as a FastAPI web service, offering an API for sepsis prediction. This setup provides a user-friendly interface where users can seamlessly input patient details and receive predictions.

ii. Docker Containerization
The application is packaged using Docker, ensuring it can be easily deployed across different environments while maintaining consistent performance and functionality.







