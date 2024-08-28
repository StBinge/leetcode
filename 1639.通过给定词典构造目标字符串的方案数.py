#
# @lc app=leetcode.cn id=1639 lang=python3
#
# [1639] 通过给定词典构造目标字符串的方案数
#
from sbw import *


# @lc code=start
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        N = len(words)
        L = len(words[0])
        T = len(target)
        Mod = 10**9 + 7

        counter = [[0] * 26 for _ in range(L)]
        for i in range(N):
            word = words[i]
            for j in range(L):
                code = ord(word[j]) - ord("a")
                counter[j][code] += 1
        f = [[0] * (L + 1) for _ in range(T + 1)]
        f[0] = [1] * (L + 1)
        for i in range(1, T + 1):
            code = ord(target[i - 1]) - ord("a")
            t = L - (T - i)
            for j in range(i, t+1):
                v = counter[j - 1][code] * f[i - 1][j - 1] + f[i][j - 1]
                f[i][j] = v % Mod
        return f[-1][-1]


# @lc code=end
assert Solution().numWays(words=["acca", "bbbb", "caca"], target="aba") == 6
assert Solution().numWays(words=["abcd"], target="abcd") == 1
assert Solution().numWays(words=["abab", "baba", "abba", "baab"], target="abba") == 16
assert Solution().numWays(words=["abba", "baab"], target="bab") == 4
