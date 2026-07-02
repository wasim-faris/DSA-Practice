



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


arr = [3,5,6,8,9,3,4]

n = len(arr)

is_swapped = False

for i in range(n):
    is_swapped = False
    for j in range(n-i-1):
        if arr[j]> arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            is_swapped = True
    if not is_swapped:
        print("array is already sorted")
        break