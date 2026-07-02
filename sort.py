



# arr = [2,5,2,7,6,9,8,3]
# n = len(arr)
# for i in range(1,n):
#     key = arr[i]
#     j = i-1
#     while j>=0 and arr[j] > key:
#         arr[j+1] = arr[j]
#         j -=1

#     arr[j+1] = key


# print(arr)


arr = [2,3,4,5,1,6,7,8,]


n = len(arr)


for i in range(1, n):
    key = arr[i]
    j = i-1
    
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j-=1

        arr[j+1] = key

print(arr)


