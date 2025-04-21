file = open("sh6.txt", "a")
for x in range(1, 101):
    file.write(f"{x}\t") 
file.close()
