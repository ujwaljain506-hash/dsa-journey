class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        count = {}

        for word in strs:
            key = tuple(sorted(word))

            if key not in count:
                count[key] = []

            count[key].append(word)

        return list(count.values())