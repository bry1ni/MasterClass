# data type\

# 1. int
my_int = 10
# 2. float
my_float = 10.0
# 3. complex
my_complex = 10 + 5j
# 4. bool
my_bool = True or False # True
my_bool = True and False # False
# 5. str
my_str = "Hello, World!"

#print("My int:"+str(my_int)+",My float"+str(my_float))
# f string
my_f_str = f"My int:{my_int}, my float: {my_float}"
#print(my_f_str)
# 6. list

my_list = [my_int, my_float, my_complex, my_bool, my_bool] # walking through the list

start = 3
end = len(my_list)
my_range = range(start, end)

for i in my_range:
    print(my_list[i])

# 7. tuple
my_tuple = (my_int, my_float, my_complex, my_bool, my_str)
#print(my_tuple)

for i in my_tuple:
    if isinstance(i, (int, float)):
        print(i)
    else:
        print("Not a number")
    break # break the loop explicitly


# 8. dict
my_dict = {
    "int": [my_int, 10],
    "float": (my_float, 10.0),
    "complex": my_complex,
    "bool": my_bool,
    "str": my_str
}

#print(my_dict)

"""for key in my_dict:
    if isinstance(my_dict[key], (list, tuple)):
        for i in my_dict[key]:
            print(i)"""

        
value = my_dict["int"]
#print(value[0])

# data type | data structure | iterable through loop

# 9. set
my_set = {my_int, my_float, my_complex, my_bool, my_str}
