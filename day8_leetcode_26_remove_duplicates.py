class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        
        for right in range (len(nums)):
            if(nums[left]==nums[right]):
                #left+=1
                #right+=1 
                #return
                pass
           
            else:
                
                left+=1
                nums[left]=nums[right]
                

                
        return left+1