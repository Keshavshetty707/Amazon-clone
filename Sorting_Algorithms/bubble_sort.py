def bsort(list,n):
    for i in range(0,n-1,1):
        for j in range(0,n-i-1,1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list
#Accept the list elements
list = []
n = int(input("Enter the number of elements: "))
print("Enter the elements: ")
for i in range(0, n):
    element = int(input())
    list.append(element)
print("Given list:", list)
asort = bsort(list,n)

print("Sorted list is: ",asort)