class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        count = {}
        for i in range(len(strs)):
            words=strs[i]
            key = tuple(sorted(words))
            if key not in count:
                count[key]=[]
            count[key].append(words)

        return list(count.values())

        

