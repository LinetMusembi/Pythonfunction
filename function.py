# Write a Python function that takes two arguments (a and b) and returns their sum.
def count_nums(a,b):
    res = a + b
    print(res)

#  2.Write a Python function that takes a string as input and returns the string reversed. 
def reverse_sentence(str):
    return str[::-1]
my_text = reverse_sentence("I am learning Python")
print(my_text)


# 3.Write a Python function that takes a list of integers as input and returns the sum of all 
# the integers in the list.

def add_all(nums):
    total = 0
    for num in nums:
        total += num
    return total

nums = [1,2,3,4,5,6]
print(add_all(nums))

# 4Write a Python function that takes a list of integers as input and returns a new list with all 
# the even numbers removed.
        
def remove_even(nums):
    num = []
    for i in nums:
        if i %2!=0:
            num.append(i)
    return num        
print(remove_even(nums=[1,2,3,4,5]))         

# 5  Write a Python function that takes a list of integers as input and returns the highest value in
#  the list. 

# 6.Write a Python function that takes a list of integers as input and returns the highest value in
# the list.

def highest_value(list1):
    highest = max(list1)
    return highest
print(highest_value(list1=[1,2,3,5,6,7,8]))


# Write a Python function that takes a list of strings as input and returns a new list with
# all the strings capitalized.
def capitalize_names(name):
    capitalize = name.upper()
    return capitalize

print(capitalize_names(name="lynet"))





