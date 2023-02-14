arr = [10,20,30,40,None,None]

size = 4
index = 1
elem = 99


def insertElement(arr,size,elem,index):
    if size == len(arr):
        print("Not enough elements to insert")
    else:
        for i in range(size,index,-1):
            arr[i] = arr[i-1]
        arr[index] = elem
    return arr

print(insertElement(arr,size,elem,index))
            