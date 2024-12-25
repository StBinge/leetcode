#
# @lc app=leetcode.cn id=2144 lang=python3
# @lcpr version=30204
#
# [2144] 打折购买糖果的最小开销
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        ret=0
        for i,c in enumerate(cost,1):
            ret+=c*(i%3!=0)
        return ret
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [6,5,7,9,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [5,5]\n
# @lcpr case=end

#

