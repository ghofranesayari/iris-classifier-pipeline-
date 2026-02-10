import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# 1. Load the data (Built-in Iris dataset)
print("Loading data...")
iris = load_iris()
X, y = iris.data, iris.target

# 2. Train the model (Logistic Regression)
print("Training model...")
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# 3. Save the 'Brain' to a file
joblib.dump(model, 'src/model.pkl')
print("✅ Success! Model saved to src/model.pkl")
