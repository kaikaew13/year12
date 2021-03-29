from random import randint

from sorting.bubblesort import bubbleSort

arr = [randint(-100,100) for i in range(10)]
print('unsorted:')
print(arr)
bubbleSort(arr)
print('sorted')
print(arr)
