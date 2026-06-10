
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


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# a = Node(10)
# b = Node(20)
# c = Node(30)

# a.next = b
# b.next = c

# # Insert 5 at beginning
# new_node = Node(5)
# new_node.next = a
# a = new_node

# # Print list
# temp = a

# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next

# print("None")

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
# a = Node(10)
# b = Node(20)
# c = Node(30)

# a.next = a
# b.next = c

# new_node = Node(5)
# new_node.next = a
# a = new_node

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# # Create nodes
# a = Node(10)
# b = Node(20)
# c = Node(30)

# # Connect nodes
# a.next = b
# b.next = c

# # New node to insert at end
# new_node = Node(40)

# # Find last node
# temp = a

# while temp.next:
#     temp = temp.next

# # Connect new node at end
# temp.next = new_node

# # Print linked list
# temp = a

# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next

# print("None")

# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
# a = Node(10)
# b = Node(20)
# c = Node(30)

# a.next = b
# b.next = c

# new_node = Node(40)

# temp = a

# while temp.next:
#     temp = temp.next

# temp.next = new_node

# temp = a

# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next
# print("None")

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
# a = Node(10)
# b = Node(20)
# c = Node(30)

# a.next = b
# b.next = c

# new_node = Node(5)

# new_node.next = a
# a = new_node

# temp = a

# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next
    
# print("None")

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
# a = Node(10)
# b = Node(20)
# c = Node(30)

# a.next = b
# b.next = c

# temp = a

# new_node = Node(40)

# while temp.next:
#     temp = temp.next
    
# temp.next = new_node

# temp = a

# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next
    
# print("None")


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
    
# a = Node(10)
# b = Node(20)
# c = Node(34)

# a.next = b
# b.next = c

# search_number = 34

# temp = a

# found = False

# while temp:
#     if temp.data == search_number:
#         found = True
#         break
#     temp = temp.next 
    

# if found:
#     print("Found")
# else:
#     print("Not found")


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# a = Node(10)
# b = Node(20)
# c = Node(30)
# d = Node(40)

# a.next = b
# b.next = c
# c.next = d

# delete_value = 30

# temp = a

# while temp.next:
#     if temp.next.data == delete_value:
#         temp.next = temp.next.next
#         break

#     temp = temp.next


# temp = a

# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next

# print("None")


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
# a = Node(10)
# b = Node(20)
# c = Node(30)
# d = Node(40)

# a.next = b
# b.next = c
# c.next = d

# temp = a

# delete_value = 10

# while temp.next:
#     if temp.next.data==delete_value:
#         temp.next = temp.next.next
#         break
    
#     temp = temp.next
    
# temp = a

# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next
    
# print("None")

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        

# a = Node(20)
# b= Node(30)
# c = Node(40)

# a.next = b
# b.next = c

# new_node = Node(44)
# new_node.next = a
# a = new_node

# temp = a

# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next
# print("None")

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
# a = Node(10)
# b = Node(20)
# c = Node(34)

# a.next = b
# b.next = c

# new_node = Node(45)

# temp = a

# while temp.next:
#     temp = temp.next
    
# temp.next = new_node

# temp = a

# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next
    
# print("None")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
a = Node(34)
b = Node(45)
c = Node(34)

a.next = b
b.next = c

new_node = Node(89)
new_node.next = a

a = new_node


temp = a

while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
    
print("None")