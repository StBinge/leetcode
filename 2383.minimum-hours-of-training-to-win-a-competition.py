#
# @lc app=leetcode.cn id=2383 lang=python3
# @lcpr version=30204
#
# [2383] 赢得比赛需要的最少训练时长
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        ret=max(sum(energy)-initialEnergy+1,0)
        for ex in experience:
            if initialExperience<=ex:
                ret+=ex+1-initialExperience
                initialExperience=ex+1
            initialExperience+=ex
        return ret
            

# @lc code=end
assert Solution().minNumberOfHours(initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1])==8
assert Solution().minNumberOfHours(initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1])==8
assert Solution().minNumberOfHours(initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1])==8


#
# @lcpr case=start
# 5\n3\n[1,4,3,2]\n[2,6,3,1]\n
# @lcpr case=end

# @lcpr case=start
# 2\n4\n[1]\n[3]\n
# @lcpr case=end

#

