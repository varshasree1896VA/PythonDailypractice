# python program to write find the sum of even and sum of odd numbers in a given list
# approach take two variables for even and odd like accumulator variables
# use  for loop and apply the even logic and store answers

# def function
def sum_even_odd_list(nums):
    even_sum = 0
    odd_sum = 0
    for i in nums:
        if i % 2 == 0:
            even_sum = i + even_sum
        else:
            odd_sum = i +odd_sum
    return even_sum,odd_sum

print(sum_even_odd_list(nums= [2,1,3,4,5]))