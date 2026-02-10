# 1. Build the Docker Image
build:
	docker build -t iris-classifier-pipeline .

# 2. Train the Model
# We use $(shell pwd) to fix the "path not found" error when running with sudo
train:
	docker run -v $(shell pwd)/src:/app/src iris-classifier-pipeline python src/train.py

# 3. Run the API Server
run:
	docker run -p 8000:8000 -v $(shell pwd)/src:/app/src iris-classifier-pipeline uvicorn src.main:app --host 0.0.0.0 --reload

# 4. Make a Prediction
predict:
	python3 src/predict.py

# 5. Clean up
clean:
	rm -f src/*.pkl
