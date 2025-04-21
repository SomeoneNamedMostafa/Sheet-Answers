file = open("sh6.txt", "r")
x = file.readlines()  
file.close()

for i in x[49:60]:  
    print(i.strip()) 