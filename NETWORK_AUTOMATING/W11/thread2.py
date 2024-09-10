import threading
from  queue import Queue
from getpass import getpass
from netmiko import ConnectHandler

USER = 'cisco'
PASSWORD = 'cisco'

routers = ['ใส่ ip sw1', 'ใส่ ip sw2', 'ใส่ ip sw3']

def ssh_session(router, output_q):
    output_dice = {}
    hostname = router
    router = {'device_type': 'cisco_ios', 'ip': router, 'username': USER, 'password': PASSWORD, 'verbose': False, }
    ssh_session = ConnectHandler(**router)
    output = ssh_session.send_command('show ip int brief')
    output_dice[hostname] = output
    output_q.put(output_dice)

if __name__ == '__main__':
    output_q = Queue()
    
    for router in routers:
        my_thread = threading.Thread(target=ssh_session, args=(router, output_q))
        my_thread.start()

    main_thread = threading.current_thread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            some_thread.join()

    while not output_q.empty():
        my_dict = output_q.get()
        for k, val in my_dict.items():
            print (k)
            print (val)