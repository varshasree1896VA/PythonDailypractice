# check is the given string a palindrome or not
# Logic: use reverse a string logic
# Then compare both strings  like original to new reversed string
# if both are equal then
# return it

# define function
def is_palindrome(s):
    reverse_string = ""
    for char in s:
        reverse_string = char + reverse_string
    if s == reverse_string:
        return True
    else:
        return False

print(is_palindrome(s="saas"))

