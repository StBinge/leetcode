#
# @lc app=leetcode.cn id=3110 lang=python3
# @lcpr version=30204
#
# [3110] 字符串的分数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(x)-ord(y)) for x,y in pairwise(s))
# @lc code=end



#
# @lcpr case=start
# "hello"\n
# @lcpr case=end

# @lcpr case=start
# "zaz"\n
# @lcpr case=end

#

