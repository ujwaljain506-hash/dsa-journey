
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0

        for right in range (len(nums)):
            if nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1







class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        left = 0
        right = 1
        max_profit = 0

        for right in range(len(prices)):
            if prices[left]>prices[right]:
                left = right
            else:
                max_profit = max(max_profit, prices[right]-prices[left])
            


        return max_profit
