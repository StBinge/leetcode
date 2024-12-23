#
# @lc app=leetcode.cn id=2706 lang=python3
# @lcpr version=30204
#
# [2706] 购买两块巧克力
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        m1=m2=100
        for p in prices:
            if p<m1:
                m1,m2=p,m1
            elif p<m2:
                m2=p
        return money if m1+m2>money else money-m1-m2
# @lc code=end



#
# @lcpr case=start
# [1,2,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [3,2,3]\n3\n
# @lcpr case=end

#

