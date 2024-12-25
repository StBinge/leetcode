#
# @lc app=leetcode.cn id=2405 lang=python3
# @lcpr version=30204
#
# [2405] 子字符串的最优划分
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def partitionString(self, s: str) -> int:
        ret=0
        mask=0
        for ch in s:
            m=1<<(ord(ch)-ord('a'))
            if mask & m:
                ret+=1
                mask=m
            else:
                mask|=m
        return ret+1
# @lc code=end



#
# @lcpr case=start
# "abacaba"\n
# @lcpr case=end

# @lcpr case=start
# "ssssss"\n
# @lcpr case=end

#

