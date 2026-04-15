# Python program to reverse integer handling both sign and overflow

# define function
def reverse_integer(x):

    sign = -1 if x < 0 else 1 # if x is a negative number stor in sign as  -1 or 1
    x = abs(x) # now absolute value removes negative sign

    rev = 0 # initialize reverse number
    while x > 0: #  check condition
        last_digit = x % 10 # get the last digit
        rev = rev * 10 + last_digit # add last digit to reverse
        x = x// 10
    rev = sign * rev # restore a sign after loop

    if rev < -2**31 or rev > 2**31-1:  # check the integer range
        return  0

    return rev # final result

print(reverse_integer(x=-1234))



