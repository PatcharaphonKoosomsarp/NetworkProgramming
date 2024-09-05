import requests
response = requests.get('https://www.google.com')
try:
    for key, value in response.headers.items():
        print('%s: %s' % (key, value))
except Exception as error:
    print('%s'%(error))
