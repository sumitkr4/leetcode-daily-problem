class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getPalindrome(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

        res = ""
        for i in range(len(s)):
            odd = getPalindrome(s, i, i)
            even = getPalindrome(s, i, i + 1)
            res = max(odd, even, res, key=len)
        return res
