# Day-5 write a python code to remove duplicates from a list
# here is the list so according to problem I need to apply logic where I should filter and remove repetitive numers or duplicate values
# so in python using list approach is good because it preserves the order and we mute or change values so to store filter new list values Iwill first take an empty list  to sote the values,
# so I will use a for loop and compare it with values in orignal list to new empty list
# so the value is not in our new list then I will append that value to empty new list and if the value alredy exists like duplicates I ignore them and finally return the new list

# define function
def remove_duplicates(nums):
     unique_list =[]
     for i in nums:
         if i not in unique_list:  # always compare value with your initialized empty list remember
            unique_list.append(i)
     return unique_list

print(remove_duplicates(nums=[4,7,1,7,4,9]))
