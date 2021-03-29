from random import randint

def bubbleSort(arr):
    for _ in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]: 
                arr[j],arr[j+1] = arr[j+1],arr[j] 

arr = [randint(-100,100) for i in range(10)]
print('unsorted:')
print(arr)
bubbleSort(arr)
print('sorted:')
print(arr)