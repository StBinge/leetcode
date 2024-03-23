#
# @lc app=leetcode.cn id=3014 lang=python3
#
# [3014] 输入单词需要的最少按键次数 I
#
from sbw import *
# @lc code=start
class Solution:
    def minimumPushes(self, word: str) -> int:
        
        time,mod=divmod(len(word),8)
        return (1+time)*time*4+(time+1)*mod
# @lc code=end
assert Solution().minimumPushes('xycdefghij')==12
assert Solution().minimumPushes('abcde')==5
