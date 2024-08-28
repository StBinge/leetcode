#
# @lc app=leetcode.cn id=2079 lang=python3
# @lcpr version=30204
#
# [2079] 给植物浇水
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cur = capacity
        ret = len(plants)
        for i, x in enumerate(plants):
            if x > cur:
                ret += i * 2
                cur = capacity
            cur -= x
        return ret


# @lc code=end
assert Solution().wateringPlants(plants=[7, 7, 7, 7, 7, 7, 7], capacity=8) == 49
assert Solution().wateringPlants(plants=[1, 1, 1, 4, 2, 3], capacity=4) == 30
assert Solution().wateringPlants(plants=[2, 2, 3, 3], capacity=5) == 14


#
# @lcpr case=start
# [2,2,3,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,4,2,3]\n4\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7,7,7,7]\n8\n
# @lcpr case=end

#
