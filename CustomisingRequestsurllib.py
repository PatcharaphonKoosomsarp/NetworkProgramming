from urllib.request import Request
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
USL = 'http://www.google.com'

def add_header():
    headers = {'Accept-Language': 'en-US,en;q=0.5',}
    Request = Request(USL, headers=headers)
    print('Request headers: ')
    for key, value in Request.headers_items():
        print("%s: %s" % (key, value))
if __name__ == '__main__':
    add_header()