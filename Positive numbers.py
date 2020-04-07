NumList = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

print("\nPositive Numbers in this List are : ")
for j in range(Number):
    if(NumList[j] >= 0):
        print(NumList[j], end = '   ')
