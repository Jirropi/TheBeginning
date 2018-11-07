import os.path
import getpass
from netmiko import ConnectHandler

username = input("Username: ")
password = getpass.getpass("Password: ")
enable = getpass.getpass("Enable: ")

print(username)
print(password)
print(enable)
