
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


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
# a = Node(34)
# b = Node(45)
# c = Node(34)

# a.next = b
# b.next = c

# new_node = Node(89)
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
        
# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)

# a.next = b
# b.next = c
# c.next = d

# head = a 
# current = head
# prev = None

# while current:
#     new_node = current.next
#     current.next = prev
#     prev = current
#     current = new_node
    
    
    
# head = prev

# temp = head

# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next
    
# print("None")


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
        
# a = Node(23)
# b = Node(56)
# c = Node(34)


# search_num = 56

# temp = a 

# found = False
# while temp.next:
#     if temp.next.data == search_num:
#         found = True
#         break
#     else:
#         found = False
        
# if found:
#     print("Element found ")
# else:
#     print("Not found the element")


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
        
# a = Node(23)
# b = Node(56)
# c = Node(34)

# largest = a


# a.next = b
# b.next = c

# temp = a

# while temp:
#     if temp.data > largest.data:
#         largest = temp
#     temp = temp.next

# print(largest.data)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
a = Node(243)
b = Node(344)
c = Node(66)
d = Node(78)
e = Node(24)

a.next = b
b.next = c
c.next = d
d.next = e

largest = a
sec_largest = a

head = a 
temp = head

while temp:
    if temp.data > largest.data:
        sec_largest = largest
        largest = temp
    elif temp.data > sec_largest.data and temp.data != sec_largest.data:
        sec_largest = temp
    temp = temp.next
        
print(f"Largest element in the linked list {largest.data}")
print(f"Secound largest element in the linkedlist {sec_largest.data}")