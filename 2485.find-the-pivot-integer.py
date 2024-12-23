#
# @lc app=leetcode.cn id=2485 lang=python3
# @lcpr version=30204
#
# [2485] 找出中枢整数
#


# @lcpr-template-start
import math

# @lcpr-template-end
# @lc code=start
class Solution:
    def pivotInteger(self, n: int) -> int:
        x=n*n+n
        if x%2:
            return -1
        x>>=1
        y=math.isqrt(x)
        if y*y==x:
            return y
        return -1
# @lc code=end



#
# @lcpr case=start
# 8\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#

