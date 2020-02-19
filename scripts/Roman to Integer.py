class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        l = list(s)
        n = len(s)
        sum = dict[l[0]]
        for a in range(n-1):
            b = a+1
            if dict[l[b]] > dict[l[a]]:
                sum = sum-2*dict[l[a]]+dict[l[b]]
            else:
                sum = sum+dict[l[b]]
        return sum