import paramiko
import time

HOST = 'ใส่ ip sw1'
user = 'cisco'
password = 'cisco'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=HOST, username=user, password=password)

print("Successful connection", +HOST)

remoite_connection = ssh_client.invoke_shell()
remoite_connection.send("en\n")
remoite_connection.send("sh ip int brief\n")
time.sleep(1)

output = remoite_connection.recv(65535)
print(output.decode())

ssh_client.close()