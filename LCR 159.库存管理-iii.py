#
# @lc app=leetcode.cn id=LCR 159 lang=python3
# @lcpr version=30204
#
# [LCR 159] 库存管理 III
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        if cnt==0:
            return []
        heap=[]
        for s in stock:
            heapq.heappush(heap,-s)
            if len(heap)>cnt:
                heapq.heappop(heap)
        return [-s for s in heap]
# @lc code=end
assert Solution().inventoryManagement([2,5,7,4],1)==[2]


#
# @lcpr case=start
# [2,5,7,4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [0,2,3,6]\n2\n
# @lcpr case=end

#

