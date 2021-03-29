def binarySearch(arr,low,high,target):
    if (low <= high):
        mid = low + int((high - low)/2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binarySearch(arr,low,mid-1,target)
        else:
            return binarySearch(arr,mid+1,high,target)
    else:
        return -1