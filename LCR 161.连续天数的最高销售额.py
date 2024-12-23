#
# @lc app=leetcode.cn id=LCR 161 lang=python3
# @lcpr version=30204
#
# [LCR 161] 连续天数的最高销售额
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSales(self, sales: List[int]) -> int:
        ret=sales[0]
        s=0
        mi=0
        for n in sales:
            s+=n
            ret=max(ret,s-mi)
            mi=min(mi,s)
        return ret
# @lc code=end



#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#

