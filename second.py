# #Question 1
# var1 = input("Enter your name: ")
# print("Good Morning",var1)

# #Question 2
# letter = '''Dear <|Name|>,
#             You are selected,
#             <|Date|>'''
# name_2 = input("Enter name:")
# date_2 = input("Enter date: ")
# letter = letter.replace('<|Name|>', name_2)
# letter = letter.replace('<|Date|>', date_2)

# print("Letter: \n", letter)

# #Question 3
# var_3 = input("Enter the test string: ")
# if (var_3.find("  ")) != -1:
#     print("There are double spaces in the given string.")
# else:
#     print("The string does not contain double spaces.")
    
# #Question 4
# var_4 = input("Enter the test string: ")
# if (var_4.find(" ")) != -1:
#     print("There are single spaces in the given string.")
# else:
#     print("The string does not contain single spaces.")

# #Question 5
# letter_5 = "Dear Shekhar,\nThis Python Course is nice.\nThanks."
# print(letter_5)

# Extra questions to practice
# # String immutability
# s = "hello"
# s[0] = "H" 
# print(s)
# # Error as string is immutable
# Right format
s = "hello"
s_1 = "H" + s[1:]
print(s_1)

# Case Conversion
s = "Python is FUN"
print(s.upper().istitle)
# lower() converts string to lower case, isupper() check if every letter is in upper case
# upper() converts string to upper case, istitle() check is every letter is every letter starts with capital or not

#String Search and replace
s = "Hello world! Hello Python"
print(s.replace("Hello", "Hi", 1))
# replace("Hello", "Hi", 1) replaces only the first occurrence of "Hello", leaving the second one unchanged.

#Split and join
words = "Python,Java,C++,JavaScript".split(",")
print(words)
print("-".join(words))

#Formatting
name = 'Alice'
print(f"My name is {name}")
