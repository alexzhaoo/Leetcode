def selectionsort(arr):
    n= len(arr)
    for j in range(n-1):
        currentmin=j
        for i in range(j+1,n):
            