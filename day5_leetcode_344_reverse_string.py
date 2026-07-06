class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left=0
        right = len(s)-1

        while left < right:
            s[right],s[left]=s[left],s[right]

            right -=1
            left +=1
            #if left == right-1:
            #    return 
            #elif left == right - 2:
            #    return
        return
            
            

s = ['h','e','l','l','o']
sol = Solution()
sol.reverseString(s)
print(s)