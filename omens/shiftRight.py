arr = [10,20,30,40,50,60,70]

def rightShift(arr):
    for i in range(len(arr)-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = None
    return arr

rightShift = rightShift(arr)
print(rightShift)