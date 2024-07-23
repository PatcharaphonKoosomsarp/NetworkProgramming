import requests

from requests.auth import HTTPBasicAuth

requests.get('http://www.google.com', auth=HTTPBasicAuth('user', 'pass'))

response = requests.get('http://www.google.com', auth=('user', 'pass'))

print('Response.status_code:'+ str(response.status_code))
if response.status_code == 200:
    print('Login successful: '+ response.text)