from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# 1. Initialize the App
app = FastAPI()

# 2. Load the trained model
# We use 'src/' because inside Docker, we are in /app, so the path is /app/src/model.pkl
model = joblib.load('src/model.pkl')

# 3. Define the Input Format
class IrisInput(BaseModel):
    features: list

# 4. Define the Prediction Endpoint
@app.post("/predict")
def predict(data: IrisInput):
    # Convert list to numpy array
    features = np.array(data.features).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(features)
    
    # Return the result
    class_name = ["setosa", "versicolor", "virginica"][int(prediction[0])]
    return {"class": class_name, "prediction": int(prediction[0])}

@app.get("/")
def read_root():
    return {"message": "Iris Model aaaa API is Live! 🌸"}
