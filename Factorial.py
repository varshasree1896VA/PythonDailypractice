# python program to find factorial of a number

# define function
def factorial(n):
    result = 1 # variable to sore final result why 1 because we cannot because multiply with zero

    for i in range(1, n+1):
            result *= i
    return result


print(factorial(n=5))

#dry run n = 5
#  i                before result(r =1)           after result(r=result*i)
#  1                    1                            r = 1x1=1
#  2                    1                                1x2=2
#  3                    2                                2x3=6
#  4                    6                                6x4=24
#  5                    24                               24x5=120
#finally  1!=1, 2!=2, 3!=6, 4!=24, 5!= 120

