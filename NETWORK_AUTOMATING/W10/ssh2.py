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

all_devices = [SW4, SW]

for device in all_devices:
    net_connect = ConnectHandler(**device)
    for n in range (2,10):
        print("Creating VLAN " + str(n))
        config_commands = ['vlan ' + str(n), 'name Python_VLAN_' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print(output)
