class Solution:
    def reverse(self, x: int) -> int:
        if x < -2 ** 31 or x > 2 ** 31 - 1:
            return 0
        L = list(str(x))
        L.reverse()

        for i in L:
            if i != '0':
                break
        index = L.index(i)
        if L[-1] == '-':
            L = L[index:-1]
            a = int("-" + "".join(L))
            if a < -2 ** 31:
                return 0
            return a
        else:
            L = L[index:]
            a = int("".join(L))
            if a > 2 ** 31 - 1:
                return 0
            return a