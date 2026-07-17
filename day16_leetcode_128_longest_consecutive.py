
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start_seq=set()
        num_set = set(nums)
        for i in range(len(nums)):
            if nums[i]-1 not in num_set:
                start_seq.add(nums[i])

        max_length = 0
        for num in start_seq:
            length = 1     
            current = num
            while (current + 1) in num_set:
                current += 1
                length += 1
            max_length = max(max_length, length)
        return max_length


        
