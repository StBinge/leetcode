#
# @lc app=leetcode.cn id=2119 lang=python3
# @lcpr version=30204
#
# [2119] 反转两次的数字
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num==0 or num%10!=0
# @lc code=end



#
# @lcpr case=start
# 526\n
# @lcpr case=end

# @lcpr case=start
# 1800\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

#

