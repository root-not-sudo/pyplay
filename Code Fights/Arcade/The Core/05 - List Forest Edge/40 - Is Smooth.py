def isSmooth(arr):

    mid = len(arr)//2
    if len(arr) % 2 == 0:
        middle_value = arr[mid] + arr[mid - 1]
    else:
        middle_value = arr[mid]
    return arr[0] == middle_value and arr[-1] == middle_value
