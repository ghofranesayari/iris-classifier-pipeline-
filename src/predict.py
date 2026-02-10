import urllib.request
import json
import ssl

# ---------------------------------------------------------
# [IMPORTANT] PASTE YOUR RENDER URL HERE
# Example: "https://iris-api-1234.onrender.com"
# ---------------------------------------------------------
host =" https://iris-classifier-pipeline.onrender.com"

# The full endpoint
url = f"{host}/predict"

# 1. The Data: A sample flower (Sepal Length, Sepal Width, Petal Length, Petal Width)
payload = {"features": [5.1, 3.5, 1.4, 0.2]}

# 2. Setup SSL context (needed for https)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# 3. Send the POST Request
try:
    print(f"🌍 Connecting to: {url}...")
    req = urllib.request.Request(
        url, 
        data=json.dumps(payload).encode(), 
        headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
    )
    response = urllib.request.urlopen(req, context=ctx)
    
    # 4. Print the result
    print("✅ Cloud Prediction Response:")
    print(response.read().decode('utf-8'))

except Exception as e:
    print(f"❌ Error: {e}")

