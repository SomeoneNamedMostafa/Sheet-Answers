file = open("sh6.txt", "r")
a = file.readlines()  
file.close()

for i in a[49:61]:  
    print(i)