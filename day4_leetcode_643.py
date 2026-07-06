class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_sum=sum(nums[:k])
        max_avg = window_sum

        for i in range (k,len(nums)):
            window_sum = window_sum - nums[i-k] + nums[i]
            max_avg = max(max_avg, window_sum)

        return max_avg/float(k)


