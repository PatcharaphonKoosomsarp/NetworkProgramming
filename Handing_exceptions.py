import urllib.error
from urllib.request import urlopen
try:
    urlopen('http://www.google.com')
except urllib.error.HTTPError as e:
    print('Exception', e)
    print('status', e.code)
    print('reason', e.reason)
    print('url', e.url)