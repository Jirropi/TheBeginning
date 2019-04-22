import device_input


device1 = device_input.device_input()
print(device1)

# save_path = input("save location: ")
# config_commands = ['show run','show inv','show ver']
#
# net_connect = ConnectHandler(**device1)
# net_connect.enable()
# hostname = net_connect.send_command("show run | hostname")
# count = 0
#
# while(len(config_commands)>count):
#     completeName = os.path.join(save_path+hostname+config_commands[count])
#     file1 = open(completeName,"w")
#     file1.write(net_connect.send_command(config_commands[count]))
#     file1.close()
#     count += 1
