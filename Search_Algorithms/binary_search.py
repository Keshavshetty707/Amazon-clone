#bsearch function iterates all the list elements to find the key element
def bsearch(list,n,key):
    low = 0
    high = n - 1
    while low <= high :
        mid =int((low+high)/2)
        if list[mid] == key:
            return mid+1
        else:
            if key < list[mid]:
                high = mid-1
            else:
                low = mid+1
    return -1

#Accept the list elements
list = []
n = int(input("Enter the number of elements: "))
print("Enter the elements: ")
for i in range(0, n):
    element = int(input())
    list.append(element)
#sort the array in case desending order elements
list.sort()
#Accept key element
key = int(input("Enter the element to be searched: "))
#call fuction lsearch
loc = bsearch(list,n,key)
#Check the loc value 
if loc == -1:
    print("Key element is not found ")
else:
    print("Key element is found at :",loc)

