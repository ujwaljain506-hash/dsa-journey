# LC 643 - Maximum Average Subarray
class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum = window_sum + nums[i] - nums[i-k]
            max_sum = max(max_sum, window_sum)
        return max_sum / float(k)


# LC 26 - Remove Duplicates from Sorted Array
class Solution(object):
    def removeDuplicates(self, nums):
        left = 0
        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
        return left + 1


# LC 167 - Two Sum II
class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        while left < right:
            sums = numbers[right] + numbers[left]
            if sums > target:
                right -= 1
            elif sums < target:
                left += 1
            else:
                return left + 1, right + 1