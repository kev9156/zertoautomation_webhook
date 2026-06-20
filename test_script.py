import requests
import json

url = "http://localhost:8000/zerto"
payload = {"vpgName": "Production_Test_VPG"}
headers = {"Content-Type": "application/json"}

try:
    print(f"Sending request to {url}...")
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"An error occurred: {e}")