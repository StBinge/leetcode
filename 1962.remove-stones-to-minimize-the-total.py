#
# @lc app=leetcode.cn id=1962 lang=python3
# @lcpr version=30204
#
# [1962] 移除石子使总数最小
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i]*=-1
        heapq.heapify(piles)
        while k and piles[0]!=-1:
            k-=1
            heapq.heapreplace(piles,piles[0]//2)
        return - sum(piles)


# @lc code=end
assert Solution().minStoneSum(piles = [4,3,6,7], k = 3) == 12
assert Solution().minStoneSum(piles=[5, 4, 9], k=2) == 12


#
# @lcpr case=start
# [5,4,9]\n2\n
# @lcpr case=end

# @lcpr case=start
# [4,3,6,7]\n3\n
# @lcpr case=end

#
