# DAY-1 Check are the two Strings are anagrams
#  Definition : when the characters and length of two are same then those strings are knows as anagrams
# CODE LOGIC: Method-1 We can solve this problem by three ways one is using two empty dictionaries then using for loop count the frequency of two string separately and comapre the  lenth of two strings if they are not equal then false meaning the strings are not anagrams else they are anagrams
# Method-2 : We can use sort method the inbuilt method and then compare both the string if equal then strings are anagrams else not
from multiprocessing.connection import Listener

# define the function:

def check_are_anagrams(s1,s2):
# check the length of two strings if not equal return false
    if len(s1) != len(s2):
        return False
# take two empty dictionaries to count the characters in the strings (s1,s2)

    freq1={}
    freq2={}
# loop the string (S1)
    for char in s1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1

# loop the string (S2)
    for char in s2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1

    return freq1 == freq2

print(check_are_anagrams(s1="listen",s2="silent"))


