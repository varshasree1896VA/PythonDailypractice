# python code to for fizzbuzz for multiples of 3 = fizz 5= buzz and multiples of 3,5 as fizzbuzz

#define function
def fizz_buzz(n):
    for i in range(1, n+1):
        if i % 3 == 0  and i % 5 == 0:
            print("fizz_buzz")
        elif i % 3 == 0 :
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

print(fizz_buzz(n=2))





