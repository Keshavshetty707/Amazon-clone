#lsearch function iterates all the list elements to find the key element
def lsearch(list,n,key):
    for i in range(0,n,1):
        if list[i] == key:
            return i+1
    return -1
#Accept the list elements
list = []
n = int(input("Enter the number of elements: "))
print("Enter the elements: ")
for i in range(0, n):
    element = int(input())
    list.append(element)
#Accept key element
key = int(input("Enter the element to be searched: "))
#call fuction lsearch
loc = lsearch(list,n,key)
#Check the loc value 
if loc == -1:
    print("Key element is not found ")
else:
    print("Key element is found at :",loc)

