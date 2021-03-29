from random import randint

from sorting.bubblesort import bubbleSort
from searching.linearsearch import linearSearch

arr = [randint(-100,100) for i in range(10)] + [5]
print('unsorted:')
print(arr)
bubbleSort(arr)
print('sorted')
print(arr)
print('searching for 5 in arr:')
print('found at index:',linearSearch(arr,5))
