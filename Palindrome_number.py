# python program to number is a given number a palindrome
# we call a number palindrome when the given number or string when read front to back and viceversa should be same
# ex: 1221 =1221 a palindrome
# 125 != 521 not palindrome
# logic


# define function
def palindrome_number(n):
    original = n
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    if original == rev:
        return True
    else:
        return False

print(palindrome_number(n=1986))




