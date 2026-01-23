# program to find the first unique character
# given a string and my job is to find the first unique character
# Method so to count or to map we can use dictionaries as it removes the duplicates and stores value in key pair

# s = "automation"
# define the function
def find_first_unique_character(s):
    freq = {}  #  Take an empty dictionary to count the character frequency
    for char in s:   # so take a for loop
        if char in freq:  # if that character is in this new empty dictionary
            freq[char] +=1  # if character already exists increment its count
        else:
            freq[char] =1  # else make its value count to one

    for char in s:
        if freq[char] == 1:
            return char


print(find_first_unique_character(s="automation"))


