#
# @lc app=leetcode.cn id=3207 lang=python3
# @lcpr version=30204
#
# [3207] 与敌人战斗后的最大分数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        mi=min(enemyEnergies)
        if currentEnergy<mi:
            return 0
        return (currentEnergy+sum(enemyEnergies)-mi)//mi
# @lc code=end



#
# @lcpr case=start
# [3,2,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2]\n10\n
# @lcpr case=end

#

