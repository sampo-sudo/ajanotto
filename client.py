import requests
import time

TARGET_URL = "http://192.168.43.246:5000/"

payload = "TIME"
response = requests.post(TARGET_URL, data=payload)
print(response.text)
