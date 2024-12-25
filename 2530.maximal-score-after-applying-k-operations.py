#
# @lc app=leetcode.cn id=2530 lang=python3
# @lcpr version=30204
#
# [2530] 执行 K 次操作后的最大分数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums=[-n for n in nums]
        heapq.heapify(nums)
        ret=0
        for i in range(k):
            ret-=heapq.heappushpop(nums,nums[0]//3)
        return ret
# @lc code=end



#
# @lcpr case=start
# [10,10,10,10,10]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,10,3,3,3]\n3\n
# @lcpr case=end

#

