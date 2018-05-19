def replaceMiddle(arr):

    if len(arr) % 2 == 0:
        arr[len(arr)//2] += arr[len(arr)//2 - 1]
        del arr[len(arr)//2 - 1]
    return arr
