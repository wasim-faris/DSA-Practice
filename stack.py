stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)

print("After Push:", stack)

# Peek
print("Top Element:", stack[-1])

# Pop
removed = stack.pop()
print("Removed:", removed)

print("After Pop:", stack)

# Size
print("Size:", len(stack))

# Empty Check
if len(stack) == 0:
    print("Stack is Empty")
else:
    print("Stack is Not Empty")



def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)


def merge(left, right):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


arr = [38, 27, 43, 3, 9, 82, 10]

sorted_arr = merge_sort(arr)

print(sorted_arr)