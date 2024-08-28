#
# @lc app=leetcode.cn id=1771 lang=python3
#
# [1771] 由子序列构造的最长回文串的长度
#


# @lc code=start
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        word = word1 + word2
        N = len(word)
        f = [[0] * N for _ in range(N)]
        ret = 0
        N1=len(word1)
        for i in range(N - 1, -1, -1):
            f[i][i] = 1
            for j in range(i + 1, N):
                if word[i] == word[j]:
                    f[i][j] = f[i + 1][j - 1] + 2
                    if i<N1<=j:
                        ret = max(ret, f[i][j])

                    continue
                f[i][j] = max(f[i + 1][j], f[i][j - 1])
        return ret


# @lc code=end
assert Solution().longestPalindrome("rhuzwqohquamvsz","kvunbxje") == 7
assert Solution().longestPalindrome("aba","cfc") == 0
assert Solution().longestPalindrome(word1 = "aa", word2 = "bb") == 0
assert Solution().longestPalindrome(word1="ab", word2="ab") == 3
assert Solution().longestPalindrome(word1="cacb", word2="cbba") == 5
