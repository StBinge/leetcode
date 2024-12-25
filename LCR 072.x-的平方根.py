#
# @lc app=leetcode.cn id=LCR 072 lang=python3
# @lcpr version=30204
#
# [LCR 072] x 的平方根
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        x0=C=float(x)
        while True:
            x1=0.5*(x0+C/x0)
            if abs(x0-x1)<1e-5:
                break
            x0=x1
        return int(x1)

# @lc code=end
assert Solution().mySqrt(8)==2
assert Solution().mySqrt(4)==2


#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 8\n
# @lcpr case=end

#

