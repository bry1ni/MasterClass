# data type\

# 1. int
# my_int = 10
# # 2. float
# my_float = 10.0
# # 3. complex
# my_complex = 10 + 5j
# # 4. bool
# my_bool = True or False # True
# my_bool = True and False # False
# # 5. str
# my_str = "Hello, World!"

# #print("My int:"+str(my_int)+",My float"+str(my_float))
# # f string
# my_f_str = f"My int:{my_int}, my float: {my_float}"
# #print(my_f_str)
# # 6. list

# my_list = [my_int, my_float, my_complex, my_bool, my_bool] # walking through the list

# start = 3
# end = len(my_list)
# my_range = range(start, end)

# for i in my_range:
#     print(my_list[i])

# # 7. tuple
# my_tuple = (my_int, my_float, my_complex, my_bool, my_str)
# #print(my_tuple)

# for i in my_tuple:
#     if isinstance(i, (int, float)):
#         print(i)
#     else:
#         print("Not a number")
#     break # break the loop explicitly


# # 8. dict
# my_dict = {
#     "int": [my_int, 10],
#     "float": (my_float, 10.0),
#     "complex": my_complex,
#     "bool": my_bool,
#     "str": my_str
# }

# #print(my_dict)

# """for key in my_dict:
#     if isinstance(my_dict[key], (list, tuple)):
#         for i in my_dict[key]:
#             print(i)"""

        
# value = my_dict["int"]
# #print(value[0])

# # data type | data structure | iterable through loop

# # 9. set
# my_set = {my_int, my_float, my_complex, my_bool, my_str}

# Functions
# def my_function():
#     print("Hello, World!")

# my_function()

# def my_function_with_args(arg1, arg2):
#     print(arg2, arg1)

# my_function_with_args("World", "Hello")

# def my_function_with_return(arg1, arg2):
#     result = arg1 + arg2
#     return result

# result = my_function_with_return(10, 20)
# print(result)

# def my_function_with_default_args(arg2=10, arg1=30):
#     return arg1 + arg2

# result = my_function_with_default_args()
# print(result)

# def my_function_with_args_kwargs(*args, **kwargs):
#     print(args)
#     print(kwargs)

# my_function_with_args_kwargs(10, 20, 30, 40, 50, name="John", age=20)

name = input("Enter your name: ")
def print_name(name):
    print(name)

print_name(name)