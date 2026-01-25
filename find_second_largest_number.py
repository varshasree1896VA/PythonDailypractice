# python program to write second largest numer

#define function:
def second_largest_num(nums):
    largest = None
    second_largest = None

    for num in nums:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest:
            if num != largest: # to handle duplicate numbers
                second_largest =num
    return second_largest

print(second_largest_num(nums = [4,7,1,9,7,9,9]))
