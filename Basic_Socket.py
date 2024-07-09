import socket

try:
    print("Fully qualified domain name: "+ socket.getfqdn("8.8.8.8"))
    print("Host name to IP address: "+ socket.gethostbyname("www.python.com"))
    print("Host name to IP address, extended: " + str(socket.gethostbyname_ex("www.python.com")))
    print("Get host name of local machine: "+ socket.gethostname())
except Exception as e:
    print("Error: "+ str(e))