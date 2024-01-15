#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        L1,L2=len(text1),len(text2)
        f=[[0]*(L2+1) for _ in range(L1+1)]
        for i in range(L1):
            for j in range(L2):
                if text1[i]==text2[j]:
                    f[i+1][j+1]=f[i][j]+1
                else:
                    f[i+1][j+1]=max(f[i+1][j],f[i][j+1])
        return f[-1][-1]
# @lc code=end

assert Solution().longestCommonSubsequence(text1 = "abc", text2 = "def")==0
assert Solution().longestCommonSubsequence(text1 = "abc", text2 = "abc")==3
assert Solution().longestCommonSubsequence(text1 = "abcde", text2 = "ace" )==3