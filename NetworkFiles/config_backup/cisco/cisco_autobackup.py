import os.path
import device_input
from netmiko import ConnectHandler


#Connects to the device, runs the show commands, 
#writes output of the commands to a file with the hostname + command as filename
def execute_backup(device):
    config_commands = ['show run','show inv','show ver']
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    hostname_from_switch = net_connect.send_command("show run | i hostname")
    split_hostname = hostname_from_switch.split()
    hostname = split_hostname[1]
    print("Executing backup for " + hostname)
    count = 0
    while(len(config_commands)>count):
        completeName = os.path.join(save_path+hostname+ " " +config_commands[count] + ".txt")
        print("Saved at " + completeName)
        file1 = open(completeName,"w")
        file1.write(net_connect.send_command(config_commands[count]))
        file1.close()
        count += 1

while True:
    input_method = int(input("Enter 1 for single entry, 2 for json file: "))
    if input_method == 1:
        device = device_input.single()
        save_path = input("save location: ")
        execute_backup(device)
        break
    elif input_method == 2:
        device_set = device_input.open_json()
        save_path = input("save location: ")
        for device in device_set:
            print(device)
            execute_backup(device)
        break
    else:
        print("Invalid Entry. Please try again.")


