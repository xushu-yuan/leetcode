"""
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

"""

# 暴力解决 - Solution 1: Find all subarrays and compare the sum
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_list = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sub_arr = [nums[k] for k in range(i, j)]
                sum_list.append(sum(sub_arr))

        return max(sum_list)


# DP (动态规划)
"""
经过DP后, nums[i]的大小为, 以原来nums[i]作为子串最后的一个元素的最大总和
思路：能否找到N-1个元素最大子序和跟N个元素最大子序和的递推关系
> S_n = max(A_n, 0) + S_n-1
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(1, n):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])

        return max(nums)


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for n in range(len(nums))]
        dp[0] = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            res = max(res, dp[i])
        return res

