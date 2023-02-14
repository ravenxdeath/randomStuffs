
arr = [10,20,30,40,50,60,70]

# def shiftLeft(arr):
#     for i in range(1,len(arr)):
#         arr[i-1] = arr[i]
#     arr[len(arr) - 1] = None
#     return arr

def shiftLeft(arr):
    for i in range(0,len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr) - 1] = None
    return arr

shiftLeft = shiftLeft(arr)
print(shiftLeft)