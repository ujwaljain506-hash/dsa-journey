class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        best_left, best_right = 0, 0

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            # Odd length
            left1, right1 = expand_from_center(i, i)
            if right1 - left1 > best_right - best_left:
                best_left, best_right = left1, right1

            # Even length
            left2, right2 = expand_from_center(i, i + 1)
            if right2 - left2 > best_right - best_left:
                best_left, best_right = left2, right2

        return s[best_left:best_right + 1]