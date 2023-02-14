arr = [10,20,30,40,50,60,90]

def rotateLeft(arr):
    temp = arr[len(arr)-1]
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = temp
    
    return arr


print(rotateLeft(arr))