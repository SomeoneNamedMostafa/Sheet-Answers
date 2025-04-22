def average(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    return sum/len(numbers)

list1=[1,2,3,4,5]
print(average(*list1))