import kagglehub
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("chaunguynnghunh/sepsis")

print("Path to dataset files:", path)

# loading data

# Use the correct path to your CSV file
data = pd.read_csv('Paitients_Files_Train.csv')
data 


