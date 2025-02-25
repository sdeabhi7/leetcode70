''' 
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

    Example 1:

    Input: nums = [1,2,3,1]
    Output: true

    Example 2:

    Input: nums = [1,2,3,4]
    Output: false
'''


def duplicates(nums):
    if len(nums) == len(set(nums)):
        return False
    else:
        return True
    
print(duplicates([1,2,4,5,2]))