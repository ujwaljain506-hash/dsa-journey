# LC 209 - Minimum Size Subarray Sum
class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        min_window = float('inf')
        sums = 0
        for right in range(len(nums)):
            sums += nums[right]
            while sums >= target:
                min_window = min(min_window, right - left + 1)
                sums -= nums[left]
                left += 1
        return 0 if min_window == float('inf') else min_window


# LC 3 - Longest Substring Without Repeating Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        window = set()
        left = 0
        max_length = 0
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length