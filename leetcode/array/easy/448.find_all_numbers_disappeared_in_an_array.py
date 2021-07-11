"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""

# Need to understand time complexity
#  O(n) runtime >> NO for loop in for loop
class Solution(object):
    def findDisappearedNumbers(self, nums):
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
                
        return [i + 1 for i, num in enumerate(nums) if num > 0]

if __name__ == "__main__":
    solution = Solution()
    nums = [4,3,2,7,8,2,3,1]
    print(solution.findDisappearedNumbers(nums))