Sepsis Prediction Project

Objective

The primary goal of this project is to predict the likelihood of a patient developing sepsis based on clinical and demographic data. The insights from this analysis aim to:
Improve early detection of sepsis in hospitals or clinics.
Optimize resource allocation for high-risk patients.
Reduce sepsis-related mortality rates by facilitating timely intervention.

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







