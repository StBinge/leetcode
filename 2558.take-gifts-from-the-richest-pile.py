#
# @lc app=leetcode.cn id=2558 lang=python3
# @lcpr version=30204
#
# [2558] 从数量最多的堆取走礼物
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts=[-g for g in gifts]
        heapq.heapify(gifts)
        while k and gifts[0]!=-1:
            heapq.heapreplace(gifts,-math.isqrt(-gifts[0]))
            k-=1
        return -sum(gifts)
            
# @lc code=end
assert Solution().pickGifts(gifts = [25,64,9,4,100], k = 4)==29


#
# @lcpr case=start
# [25,64,9,4,100]\n4\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1]\n4\n
# @lcpr case=end

#

