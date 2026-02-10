import joblib
import numpy as np

def test_prediction():
    # 1. Load the trained model
    print("🧪 Loading model...")
    model = joblib.load('src/model.pkl')
    
    # 2. Run a dummy prediction
    data = np.array([[5.1, 3.5, 1.4, 0.2]])
    prediction = model.predict(data)
    
    # 3. Assert the result is valid
    assert prediction[0] in [0, 1, 2]
    print("✅ System Test Passed: Model produces valid predictions.")

if __name__ == "__main__":
    test_prediction()
