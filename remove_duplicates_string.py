# python program to remove duplicates in a string
# Method since strings ae immutable we can take a new empty string and use a for loop
# apply conditionals and check whether the char is already exists or not
# we can also use set approach and also dictionaries

# define funtion
def remove_all_duplicates_string(s):
    result = ""  # initialize an empty string to store the final answer
    for char in s:     # use for loop to the given string
        if char not in result:  # applying if condition to check whether character exists in this new empty string
            result += char
    return result


print(remove_all_duplicates_string(s="programming"))
