'''
    Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

    Example 1:

    Input: nums = [3,0,1]
    Output: 2

    Example 2:

    Input: nums = [0,1]
    Output: 2
'''

def missingnumber(nums):
    max_num = max(nums)
    for i in range(max_num + 2):
        if i not in nums:
            return i


def missingnumber(nums):
    nums.sort()
    for i,j in enumerate(nums):
        if i != j:
            return i
        if j == len(nums)-1:
            return j+1

# The most optimized solution
def missingnumber(nums):
    return sum(range(len(nums)+1)) - sum(nums)
            

print(missingnumber([0,1,2,3,4]))