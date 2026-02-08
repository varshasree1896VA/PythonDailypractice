#fibanacci for nth value python program

#define function
def fibonacci_nth(n):
    a,b = 0, 1
    if n <= 1:
      return n

    for _ in range (2,n+1):
        a,b = b, a+b
    return b

print(fibonacci_nth(6))

#dry run n=6 i.e. 2,3,4,5
#    n                       a                  b=fib(n)
#    0                       0                  fib(0th)=0
#    1                       1                  fib(1th)=1
#    2                       1                  fib(2nd)= 0+1 =1
#    3                       1                    b= 1+1=2
#    4                       2                    b=2+3=5
#    5                       5                    b=5+3=8
#    fib(6th) = 8





