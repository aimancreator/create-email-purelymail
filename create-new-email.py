import requests
import json

url = 'https://purelymail.com/api/v0/createUser'

data = {  # Replace with your actual data
    "userName": "mynamesistar",  # User's ID before the @.
    "domainName": "placeq.com",  # Domain after the @.
    "password": "rista123456",  # User's password.
    "enablePasswordReset": False,  # Allow password reset
    "recoveryEmail": "",  # Email for recovery.
    "recoveryEmailDescription": "Email recovery",  # Description for recovery email.
    "recoveryPhone": "",  # Phone for recovery.
    "recoveryPhoneDescription": "Phone recovery",  # Description for recovery phone.
    "enableSearchIndexing": True,  
    "sendWelcomeEmail": True  # Send welcome email
}

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'Purelymail-Api-Token': 'your api key'  # Replace with your actual API token
}

try:
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

except requests.exceptions.RequestException as e:
    print("Error:", e)
    if response is not None:
      print("Response Text:", response.text)