class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        first=strs[0]
        last=strs[-1]
        for i in range(len(first)):
            if first[i]==last[i]:
                i+=1
            else:
                return first[:i]
        return first
            