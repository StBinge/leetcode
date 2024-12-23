#
# @lc app=leetcode.cn id=3259 lang=python3
# @lcpr version=30204
#
# [3259] 超级饮料的最大强化能量
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        fa,fb=energyDrinkA[0],energyDrinkB[0]
        for i in range(1,len(energyDrinkA)):
            fa,fb=max(fa+energyDrinkA[i],fb),max(fb+energyDrinkB[i],fa)
        return max(fa,fb)
# @lc code=end
assert Solution().maxEnergyBoost(energyDrinkA = [1,3,1], energyDrinkB = [3,1,1])==5


#
# @lcpr case=start
# [1,3,1]\n[3,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,1,1]\n[1,1,3]\n
# @lcpr case=end

#

