# LC 3 - Longest Substring Without Repeating Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        window = set()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            max_len = max(max_len, right - left + 1)
        
        return max_len


# LC 438 - Find All Anagrams in a String
class Solution(object):
    def findAnagrams(self, s, p):
        if len(s) < len(p):
            return []
        result = []
        p_count = {}
        window_count = {}
        for i in range(len(p)):
            p_count[p[i]] = p_count.get(p[i], 0) + 1
            window_count[s[i]] = window_count.get(s[i], 0) + 1
        
        if p_count == window_count:
            result.append(0)
        
        for i in range(len(p), len(s)):
            char_in = s[i]
            window_count[char_in] = window_count.get(char_in, 0) + 1
            char_out = s[i - len(p)]
            window_count[char_out] = window_count.get(char_out, 0) - 1
            
            if window_count[char_out] == 0:
                del window_count[char_out]
            
            if window_count == p_count:
                result.append(i - len(p) + 1)

        return result