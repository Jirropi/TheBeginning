

ipSource = open("C:/Users/jirro/OneDrive/Desktop/Files/IPs.txt")
ipList = ipSource.readlines()
for each_line in ipList:
    count = 0
    line = each_line
    split_line = line.split(",")
    print (split_line[count])
    count += 1
    print (split_line[count])


