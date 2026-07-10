class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1=0
        index2=len(numbers)-1
        
        
        while index1<index2:
            sums=numbers[index1]+numbers[index2]
            
            if(target == sums):
                return index1+1,index2+1
            elif(target>sums):
                index1+=1
            elif(target<sums):
                index2-=1