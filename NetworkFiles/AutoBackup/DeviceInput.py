import getpass
import socket


# Function collects IP,username,password and enable and
# returns a set needed for netmiko
def DeviceInput():
    print()
    while True:
        ip = input("ip Address: ")
        try:
            socket.inet_aton(ip)
            break
        except socket.error:
            print("ip address invalid. please try again")
    username = input("username: ")
    password = getpass.getpass("password: ")
    enable = getpass.getpass("enable: ")
    deviceSet = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': username,
        'password': password,
        'secret': enable}
    return deviceSet
