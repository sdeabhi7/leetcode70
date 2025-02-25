'''
    Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, 
    for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
    Return the answer in an array.

    Example 1:

    Input: nums = [8,1,2,2,3]
    Output: [4,0,1,1,3]

    Example 2:

    Input: nums = [6,5,4,8]
    Output: [2,1,0,3]
'''


def smallerNumbersThanCurrent(nums):
    greater = []
    for i in nums:
        temp = 0
        for j in nums:
            if i > j:
                temp += 1
        greater.append(temp)
    return greater

# optimized approach
def smallerNumbersThanCurrent(nums):
    temp = nums.copy()
    temp.sort()
    d = {}
    for i,j in enumerate(temp):
        if j not in d:
            d[j] = i
    greater = []
    for i in nums:
        greater.append(d[i])
    return greater

print(smallerNumbersThanCurrent([8,1,2,2,3]))