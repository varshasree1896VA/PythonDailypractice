# sum logic according to we need to find value from the given list of numbers match with target value
# we use dictionaries to check is the value being with target value and store it
# x +y = sum
#

#define function
def two_sum(nums, target):
    result = {} # dictionary to number like the values we have seen already (memory)
    for i, n in enumerate(nums): # loop through the list with n and index
        needed_number = target - n # find the needed number to get the target value
        if needed_number in result: # check if number is already seen
            return [result[needed_number], i] # if found indices and return
        result[n] = i # if not store the number with its index

print(two_sum(nums=[2, 7, 11, 5], target=9))

#dry  run
#  iteration             i          n          needed_number (target-n)          result{}
#   1                    0          2           9-2 = 7                          {2:0}
#    2                   1           7          9-7= 2   (already exists)
#   return [result] = {2:0}, (i) 1 =7
#   finally [0,1] = {2:0, 7:1} =2+7 =9
#
#