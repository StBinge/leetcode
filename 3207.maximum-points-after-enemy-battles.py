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
        # mi,mid=enemyEnergies[0],0
        # for i in range(1,len(enemyEnergies)):
        #     if enemyEnergies[i]<mi:
        #         mi=
        mi=min(enemyEnergies)
        if mi>currentEnergy:
            return 0
        return (sum(enemyEnergies)+currentEnergy)//mi -1
# @lc code=end
assert Solution().maximumPoints([2],10)==5
assert Solution().maximumPoints([3,2,2],2)==3


#
# @lcpr case=start
# [3,2,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2]\n10\n
# @lcpr case=end

#

