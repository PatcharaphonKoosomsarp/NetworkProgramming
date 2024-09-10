from netmiko import ConnectHandler

SW4 = {
    'device_type': 'cisco_ios',
    'ip': 'ip ของ sw4',
    'username': 'cisco',
    'password': 'cisco',
}

SW = {
    'device_type': 'cisco_ios',
    'ip': 'ip ของ sw5',
    'username': 'cisco',
    'password': 'cisco',
}

f = open('')
line = f.read().splitlines()
print(line)

all_devices = [SW4, SW]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_coonfig_set(line)
    print(output)