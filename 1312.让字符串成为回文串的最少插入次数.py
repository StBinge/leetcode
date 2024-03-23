#
# @lc app=leetcode.cn id=1312 lang=python3
#
# [1312] 让字符串成为回文串的最少插入次数
#
from sbw import *
# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        L=len(s)

        f=[[0]*(L) for _ in range(L)]
        for span in range(2,L+1):
            for i in range(L-span+1):
                j=i+span-1
                if s[i]==s[j]:
                    f[i][j]=f[i+1][j-1]
                else:
                    f[i][j]=min(f[i+1][j],f[i][j-1])+1
 
        return f[0][-1]
# @lc code=end
assert Solution().minInsertions(s = "leetcode")==5
assert Solution().minInsertions(s = "mbadm")==2
assert Solution().minInsertions(s = "zzazz")==0
