class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        maxl = length = len(s)
        while maxl:
            n = length - maxl + 1
            while n:
                substr = s[n - 1:n + maxl - 1]
                if substr == substr[::-1]:
                    return substr
                n = n - 1
            maxl = maxl - 1
        return ""


solution = Solution()
l = solution.longestPalindrome("babad")
print(l)