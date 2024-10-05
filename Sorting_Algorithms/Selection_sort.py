def Ssort(list,n):
    for i in range(1,n,1):
        small = list[i-1]
        pos = i-1
        for j in range(i,n,1):
            if list[j] < small:
                small = list[j]
                pos = j
        temp = list[i-1]
        list[i-1] = list[pos]
        list[pos] = temp
    return list
#Accept the list elements
list = []
n = int(input("Enter the number of elements: "))
print("Enter the elements: ")
for i in range(0, n):
    element = int(input())
    list.append(element)
print("Given list:", list)
asort = Ssort(list,n)

print("Sorted list is: ",asort)