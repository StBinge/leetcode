#
# @lc app=leetcode.cn id=2169 lang=python3
# @lcpr version=30204
#
# [2169] 得到 0 的操作数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ret=0
        if num1>num2:
            num1,num2=num2,num1
        while num1:
            d,m=divmod(num2,num1)
            ret+=d
            num1,num2=m,num1
        return ret
# @lc code=end

assert Solution().countOperations(2,3)==3

#
# @lcpr case=start
# 2\n3\n
# @lcpr case=end

# @lcpr case=start
# 10\n10\n
# @lcpr case=end

#

