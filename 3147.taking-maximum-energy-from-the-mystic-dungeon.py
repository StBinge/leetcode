#
# @lc app=leetcode.cn id=3147 lang=python3
# @lcpr version=30204
#
# [3147] 从魔法师身上吸取的最大能量
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        for i in range(k, len(energy)):
            energy[i % k]=max(energy[i%k],0)+ energy[i]
        return max(energy[:k])


# @lc code=end
assert Solution().maximumEnergy([-2,-3,-1],2) == -1
assert Solution().maximumEnergy(energy=[5, 2, -10, -5, 1], k=3) == 3


#
# @lcpr case=start
# [5,2,-10,-5,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [-2,-3,-1]\n2\n
# @lcpr case=end

#
