L = []
n = int(input("Enter no.of elemnts in list : "))
for i in range(0, n):
    num = int(input("Enter the element to be inserted : "))
    L.append(num)
sum = 0
for x in range(0, n):
    sum = sum + (int(L[x])*int(L[x]))

print("Sum of list elements : ", sum)
