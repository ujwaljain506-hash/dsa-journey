class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = 0
        count = 0
        seen = {0: 1}  # important: we start with 0 seen once

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if (prefix_sum - k) in seen:
                count += seen[prefix_sum - k]

            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

        
        return count