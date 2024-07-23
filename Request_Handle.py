import requests

data_dictionary = {'customer': 'martin', 'custtel': '32232', 'size': 'lagre', 'custmail': 'main@domain.com'}

response = requests.post('http://www.google.com', data=data_dictionary)
print("HTTP Status Code:"+ str(response.status_code))
if response.status_code == 200:
    print(response.text)