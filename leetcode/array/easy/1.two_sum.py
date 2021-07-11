"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_end = len(nums)
        result = []
        for i in range(nums_end):
            number = nums[i]
            for j in range(i+1, nums_end):
                if number + nums[j] == target:
                    return [i, j]
        raise Exception("No two sum solution")
            