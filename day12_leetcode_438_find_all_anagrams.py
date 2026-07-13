class Solution(object):
    def findAnagrams(self, s, p):
    
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        result=[]
        p_count = {}
        for char in p:
            p_count[char] = p_count.get(char, 0) + 1
        
        window_count = {}

        for i in range(len(p)):
            ch = s[i]
            window_count[ch] = window_count.get(ch, 0) + 1
            
        if window_count == p_count:
            result.append(0)
            
        for i in range(len(p),len(s)):
            char_in = s[i]
            window_count[char_in] = window_count.get(char_in, 0) + 1
            
            char_out = s[i-len(p)]
            window_count[char_out] = window_count.get(char_out, 0) - 1
            #window_count[char_out] -= 1

            if window_count[char_out] == 0:
                del window_count[char_out]
            if window_count == p_count:
                result.append(i - len(p) + 1)
        return result


