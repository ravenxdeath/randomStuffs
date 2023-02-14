arr = [10,20,30,40,50,60,90]

def rotateLeft(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[len(arr)-1] = temp
    
    return arr


print(rotateLeft(arr))