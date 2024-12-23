#
# @lc app=leetcode.cn id=面试题 01.09 lang=python3
# @lcpr version=30204
#
# [面试题 01.09] 字符串轮转
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1)==len(s2) and (s1+s1).find(s2)!=-1
# @lc code=end



#
# @lcpr case=start
# "waterbottle"\n"erbottlewat"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"aba"\n
# @lcpr case=end

#

