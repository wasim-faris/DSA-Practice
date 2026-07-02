



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


arr = [4,5,6,7,6,7,98,1,3,2,5]


n = len(arr)
swap_count = 0

for i in range(n):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swap_count +=1

print(f"total swap count {swap_count}")


