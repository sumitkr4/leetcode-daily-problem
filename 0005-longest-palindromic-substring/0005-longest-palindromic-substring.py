class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n <= 1:
            return s

        max_length = 1
        curr_string = s[0]

        for i in range(n):

            # Odd-length palindrome
            left = i - 1
            right = i + 1

            while left >= 0 and right < n and s[left] == s[right]:

                curr_length = right - left + 1

                if curr_length > max_length:
                    max_length = curr_length
                    curr_string = s[left:right + 1]

                left -= 1
                right += 1

            # Even-length palindrome
            left = i
            right = i + 1

            while left >= 0 and right < n and s[left] == s[right]:

                curr_length = right - left + 1

                if curr_length > max_length:
                    max_length = curr_length
                    curr_string = s[left:right + 1]

                left -= 1
                right += 1

        return curr_string