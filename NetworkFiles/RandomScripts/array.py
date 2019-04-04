array1 = []
flag = True
while flag:
    input1 = input("add smthn: ")
    if input1 == "end":
        flag = False
    else:
        array1.append(input1)

for i in range(len(array1)):
    print (array1[i])