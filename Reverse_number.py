# python code to reverse a number
# logic we need to use modular division to get egt last digit
# division for removing the last digit

# define function
def reverse_number(n):
    rev = 0 #

    while n > 0:
        digit = n % 10 # get the last digit
        rev = rev * 10 + digit # add to get reverse value
        n = n // 10  # remove the last digit
    return rev

print(reverse_number(n=152))

    # dry run
    # step    n=n//10       rev = rev*10 + digit
    # start     152               -
    #  1        15                2
    #  2         1                5
    #  3         0                1
    #finally reverse number = 251