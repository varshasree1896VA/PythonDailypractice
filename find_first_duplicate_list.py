# python program to find the first duplicate in a list

# def the function
def first_duplicate_number(nums):
    freq = {}
    for num in nums:     # Step 1: Count frequency of each number

        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for num in nums:        # Step 2: Find the first number with frequency 1

        if freq[num] == 1:
            return num
    return None           #Step 3: If no non-repeating number found


print(first_duplicate_number(nums = [2, 5, 1, 2, 3, 5]))


# Approach two :we can also use counters will automatically count all numbers and then we can use for loop and then numbers whose value is equal to 1 then return that




