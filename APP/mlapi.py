from fastapi import FastAPI, File, UploadFile, HTTPException
import pandas as pd
import numpy
from typing import Dict
import joblib
import uvicorn
 
app = FastAPI(
    title= "An application to predict Sepsis",
    description= "This application can be used to predict likelihood of developing sepsis"
)
 
MODEL_PATHS = {
    "LogisticRegression": "Models/Logistic Regression_best_model.pkl",
    "RandomForest": "Models/Random Forest_best_model.pkl"
}

 
# loading models
Models = {}
for model, path in MODEL_PATHS.items():
    try:
        Models[model] = joblib.load(path)
    except Exception as e:
        raise RuntimeError(f"Failed to load model '{model}' from '{path}'. Error: {e}")
 
@app.get("/")
async def st_endpoint():
    return{"message": "Welcome to Sepsis prediction App"} 

 
@app.post("/predict")
async def predictor(model: str, file: UploadFile = File(...)):
    """
    accept a model
    load a file
 
    return a json with the prediction for each row
    """
 
#loading csv file
    try:
        data = pd.read_csv(file.file)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading file {e}")
   
    if model not in Models:
        raise HTTPException(status_code=400, detail=f"Model {model} not found")
 
 
    #verify required features
    required_features = Models[model].n_features_in_
    if len(data.columns) != required_features:
        raise HTTPException(status_code=400, detail=f"Invalid number of features. Expected {required_features}, got {len(data.columns)}columns.")
 
    # convert to array
    # features =data.values
   
    #model selection
    selected_model = Models[model]
 
    #prediction
    try:
        predictions = selected_model.predict(data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error during prediction")
   
    #show response
    results = {
        "model_used" : model,
        "predictions" : predictions.tolist()
 
        }
 
    return results
 
if __name__ == "__main__":
    uvicorn.run("mlapi:app", reload=True)
   
 

 

  
