2345 

# def changin_to_string(s):
#      if s == "":
#          return 0
     
#      return int(s[0]) + changin_to_string(s[1:])
 
# print(changin_to_string("1234"))

# # def digit_sum(s):
# #     if s == "":
# #         return 0

# #     return int(s[0]) + digit_sum(s[1:])

# print(digit_sum("123"))


def reverse_string(s):
    if s == "":
        return 0
    
    return s + reverse_string(s[::-1])
    
print(reverse_string("hello"))