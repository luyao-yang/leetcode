class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if strs == []:
            return ""
        shortest = min(strs, key=len)
        n = len(shortest)

        for i in range(n):
            for str in strs:
                if str.startswith(shortest) is False:
                    shortest = shortest[:-1]

        return shortest


solution = Solution()
solution.longestCommonPrefix(["babb", "caa"])