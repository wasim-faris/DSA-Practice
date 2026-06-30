arr = [23,4,567,89,1,4,89,12,233,1,22]
n = len(arr)
count = 0
for i in range(n):
    print(arr)
    for j in range(0, n-1-i):
        if arr[j] > arr[j+1]:
            count+=1
            arr[j], arr[j+1] = arr[j+1], arr[j]

    print(f"after pass:- {i+1} arr is {arr}")


