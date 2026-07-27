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