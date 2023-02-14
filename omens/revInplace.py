arr = [10,20,30,40,50,60,70]

def revInPlace(arr):
    i = 0
    j = len(arr)-1
    
    while i < j :
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        
        i += 1
        j -= 1
    print(arr)
    return arr

revInPlace(arr)
   

