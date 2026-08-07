class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start_seq = set()
        nums_set = set(nums)
        
        for i in range(len(nums)):
            if nums[i]-1 not in nums_set:
                start_seq.add(nums[i])

        max_len = 0
        for num in start_seq:
            length = 1
            current = num
            while current + 1 in nums_set:
                length += 1
                current += 1
            max_len = max(max_len, length)   # ← moved outside while, still inside for

        return max_len