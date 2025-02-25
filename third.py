# #question 1
# fruit_1 = []
# for i in range(7):
#     fruit = input(f"Enter Fruit {i+1}: ")
#     fruit_1.append(fruit)
    
# print("Fruits List: ", fruit_1)

# # Question 2
# marks_2 = []
# for i in range(6):
#     mark = int(input(f"Enter the marks of student {i+1}: "))
#     marks_2.append(mark)

# marks_2.sort()
# print("Marks list(Sorted): ",marks_2)

# # Question 3
# var_3 = (1,2,3,4)
# print(var_3)
# # Changing tuple is not possible
# var_3[0] = 5
# print(var_3)

# # Question 4
# list_4 = [1,2,3,4]
# sum_of_list = 0
# for i in range(4):
#     sum_of_list += list_4[i]
    
# print(sum_of_list) 

## Question 5
tuple_5 = (7,0,8,0,0,9)
# count = 0
# for i in tuple_5:
#     if i ==0:
#        count = count+1
        
# print("Number of zeros in tuple: ", count)
# Alternate approach
count_zeros = tuple_5.count(0)
print("Number of zeroes: ", count_zeros)