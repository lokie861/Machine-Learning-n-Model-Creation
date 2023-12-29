from random import randint
import time

Values = []

def binary_search(arr,low, high, x):
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1


inx = 5345223
lenght = 10000000
for x in range(lenght):
    Values.append(x)


val = list(set(Values))
start = time.time()

result = binary_search(Values,0,len(Values)-1,inx)

end = time.time()

print("Binary search",end - start,result)
start1 = time.time()
for x in range(len(Values)):
    if x == inx:
        result1 = x
        break
    else:
        result1 = -1
end1 = time.time()
print("Linear search",end1 - start1,result1)