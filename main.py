from random import randint

from sorting.bubblesort import bubbleSort
from searching.linearsearch import linearSearch
from searching.binarysearch import binarySearch

arr = [randint(-100,100) for i in range(10)] + [5]
print('unsorted:')
print(arr)
bubbleSort(arr)
print('sorted')
print(arr)
print('searching for 5 in arr using linear search:')
print('found at index:',linearSearch(arr,5))
print('searching for 5 in arr using binary search:')
print('found at index:',binarySearch(arr,0,len(arr)-1,5))
