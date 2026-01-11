# write a program to reverse a string
# logic:
# Method-1 take a empty string because string are immutable we can change the value of a string inplace so to reverse the string we nee to apply prepending char in forward dirctions so string is reversed and then return it using  a for loop
# Method-2 we can also solve this problem by using two pointer by using a while loop
# method-3 We can also solve by using inbuilt method also


# define function
def reverse_string(s):
    new_reversed_string =""   # Initialized an empty string
    for char in s:    # looping for each character in the given string
        new_reversed_string = char + new_reversed_string   # applying the prepending character logic for string reversal
    return new_reversed_string # finally, return the updated reversed new string

print(reverse_string(s="python code"))