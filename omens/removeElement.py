arr = [10,6,8,11,15,20]
#want to remove 8 which is at index 2

def removeElement(arr,index,size):
    for i in range(index+1,size):
        arr[i] = arr[i+1]
    arr[size] = None
    return arr

print(removeElement(arr,2,5))