
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
# a = Node(30)
# b = Node(23)
# c = Node(50)

# a.next = b
# b.next = c

# temp = a

# while temp:
#     print(temp.data , end=" ")
#     temp = temp.next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node(10)
b = Node(20)
c = Node(30)

a.next = b
b.next = c

# Insert 5 at beginning
new_node = Node(5)
new_node.next = a
a = new_node

# Print list
temp = a
print(a.data)

while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")
    