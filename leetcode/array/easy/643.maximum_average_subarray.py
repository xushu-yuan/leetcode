"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.


"""


# find all sub arrays
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        max_sum = sum([nums[i] for i in range(k)])
        for i in range(n-k+1):
            sub_arr = [nums[j] for j in range(i,i+k)]
            max_sum = max(max_sum, sum(sub_arr))
            print(sub_arr)
        return float(max_sum/k)

"""
Sliding window
Instead of creating a cumulative sum array first, and then traversing over it to determine the required sum, we can simply traverse over numsnums just once, and on the go keep on determining the sums possible for the subarrays of length kk. To understand the idea, assume that we already know the sum of elements from index ii to index i+ki+k, say it is xx.
Now, to determine the sum of elements from the index i+1i+1 to the index i+k+1i+k+1, all we need to do is to subtract the element nums[i]nums[i] from xx and to add the element nums[i+k+1]nums[i+k+1] to xx. We can carry out our process based on this idea and determine the maximum possible average.
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)
        max_sum = sum([nums[i] for i in range(k)])
        for i in range(k, n):
            max_sum = max(max_sum,max_sum+(nums[i]-nums[i-k]));
        
        return max_sum/k;


if __name__ == "__main__":
    s = Solution()
    nums = [1,12,-5,-6,50,7]
    k = 4
    print(s.findMaxAverage(nums, k))