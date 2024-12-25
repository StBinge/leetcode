#
# @lc app=leetcode.cn id=2240 lang=python3
# @lcpr version=30204
#
# [2240] 买钢笔和铅笔的方案数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        cnt1=0
        ret=0
        while cnt1*cost1<=total:
            ret+=(total-cnt1*cost1)//cost2 + 1
            cnt1+=1
        return ret
# @lc code=end



#
# @lcpr case=start
# 20\n10\n5\n
# @lcpr case=end

# @lcpr case=start
# 5\n10\n10\n
# @lcpr case=end

#

