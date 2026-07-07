class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lef1=0
        for lef2 in range(0,len(nums)):
         if nums[lef2] != 0:
            nums[lef1],nums[lef2] = nums[lef2],nums[lef1]
            lef1 +=1


nums=[0,1,5,0,9]
sol=Solution()
sol.moveZeroes(nums)
print(nums)