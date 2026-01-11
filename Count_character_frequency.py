# write a python code to count frequency of characters in a string
# logic: I need to count how many times each character comes in the given string , so am using an empty dictionary so that Ican get the key and value of each charcter for string and then loop it and then compare it with the original string and then if char alredy exists Iwill increemnt frequency count or else update it with one and then fnaaly return the dictionary

# define function
def count_char_frequency(s):
    freq = {}   # initialized an empty dictionary t
    for char in s:  # looping for each character on the given string
        if char in freq:   # condition
            freq[char] +=1    # if char already exists increment, the count
        else:
            freq[char] =1   #  if  nor update count to 1
    return freq   # finally, return the empty dictionary

print(count_char_frequency(s="programing"))