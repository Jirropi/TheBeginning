import getpass
import socket
import json


# Function collects IP,username,password and enable and
# returns a set needed for netmiko
def single():
    print()
    while True:
        protocol = int(input("1 for SSH, 2 for Telnet. Please enter type (1/2): "))
        if protocol == 1:
            while True:
                ip = input("ip Address: ")
                if ip.count('.') == 3:
                    try:
                        socket.inet_aton(ip)
                        break
                    except socket.error:
                        print("ip address invalid. please try again")
                else:
                    print("ip address invalid. please try again")
            username = input("username: ")
            password = getpass.getpass("password: ")
            enable = getpass.getpass("enable: ")
            device_set = {
                'device_type': 'cisco_ios',
                'ip': ip,
                'username': username,
                'password': password,
                'secret': enable}
            return device_set
        elif protocol == 2:
            while True:
                ip = input("ip Address: ")
                if ip.count('.') == 3:
                    try:
                        socket.inet_aton(ip)
                        break
                    except socket.error:
                        print("ip address invalid. please try again")
                else:
                    print("ip address invalid. please try again")
            password = getpass.getpass("password: ")
            enable = getpass.getpass("enable: ")
            device_set = {
                'device_type': 'cisco_ios_telnet',
                'ip': ip,
                'password': password,
                'secret': enable}
            return device_set
        else:
            print("Invalid Entry. Try Again")

#Opens a JSON file that contains details needed for netmiko
def open_json():
    json_input = input("Full path to file: ")
    device_set = json.load(open(json_input))
    return device_set
#End
