import requests

def check_httponly(c):
    if 'httponly' in c.rest.keys:
        return True
    else:
        return False
cookies = []
url = 'http://github.com'
response = requests.get(url)

for cookie in response.cookies:
    print('Name :', cookie.name)
    print('Value :', cookie.value)
    cookie.append(cookie.value)
    if not cookie.secure:
        cookie.secure = False
    print('HTTPOnly', check_httponly(cookie), '\n')
print(set(cookies))
    