import paramiko

hostname = "192.168.1.124"
port = 22
user = "Patcharaphon"
passwd = "12345"

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    client.connect(hostname, port, user, passwd)
    while True:
        try:
            cmd = input("Enter command: ")
            stdin, stdout, stderr = client.exec_command(cmd)
            print(stdout.read().decode())
        except KeyboardInterrupt:
            break
    client.close()
except Exception as err:
    print(str(err))