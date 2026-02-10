# --------------------------------------------------------------------
# 🛠️ SETUP & LOCAL DEV (Run these on your laptop)
# --------------------------------------------------------------------

# Install all dependencies (Streamlit, FastAPI, etc.) locally
install:
	pip install -r requirements.txt

# Run the Streamlit Frontend (The Website)
app:
	streamlit run src/frontend.py

# Run the Test Script locally
test:
	python src/test_model.py

# Make a prediction using the script (Calls the Cloud API)
predict:
	python3 src/predict.py

# --------------------------------------------------------------------
# 🐳 DOCKER OPERATIONS (Run these to build/ship the container)
# --------------------------------------------------------------------

# Build the Docker Image
build:
	docker build -t iris-classifier-pipeline .

# Train the model INSIDE Docker (ensures reproducibility)
train:
	docker run -v $$(pwd)/src:/app/src iris-classifier-pipeline python src/train.py

# Run the API Server INSIDE Docker (for local testing before cloud)
run:
	docker run -p 8000:8000 -v $$(pwd)/src:/app/src iris-classifier-pipeline uvicorn src.main:app --host 0.0.0.0 --reload

# --------------------------------------------------------------------
# 🧹 UTILITIES
# --------------------------------------------------------------------

# Clean up generated files
clean:
	rm -f src/*.pkl
	rm -rf __pycache__
