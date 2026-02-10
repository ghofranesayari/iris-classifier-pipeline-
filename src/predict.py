import urllib.request
import json

# 1. The URL of our API (running in Docker)
url = "http://localhost:8000/predict"

# 2. The Data: A sample flower (Sepal Length, Sepal Width, Petal Length, Petal Width)
# This is a "Setosa" flower.
payload = {"features": [5.1, 3.5, 1.4, 0.2]}

# 3. Send the POST Request
try:
    req = urllib.request.Request(
        url, 
        data=json.dumps(payload).encode(), 
        headers={'Content-Type': 'application/json'}
    )
    response = urllib.request.urlopen(req)
    
    # 4. Print the result
    print("✅ Prediction Response:")
    print(response.read().decode('utf-8'))

except Exception as e:
    print(f"❌ Error: Could not connect to API. Is 'make run' running in another terminal?\nDetails: {e}")
