#
# @lc app=leetcode.cn id=1668 lang=python3
#
# [1668] 最大重复子字符串
#
from sbw import *
# @lc code=start
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        sl,wl=len(sequence),len(word)
        f=[0]*sl
        for i in range(wl-1,sl):
            if sequence[i-wl+1:i+1]==word:
                f[i]=1+f[i-wl]
        return max(f)
# @lc code=end
assert Solution().maxRepeating('aaabaaaabaaabaaaabaaaabaaaabaaaaba',"aaaba")==5
