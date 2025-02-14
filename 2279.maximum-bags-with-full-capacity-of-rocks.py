#
# @lc app=leetcode.cn id=2279 lang=python3
# @lcpr version=30204
#
# [2279] 装满石头的背包的最大数量
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumBags(
        self, capacity: List[int], rocks: List[int], additionalRocks: int
    ) -> int:
        if sum(capacity) <= sum(rocks) + additionalRocks:
            return len(capacity)
        needs=sorted([c-r for c,r in zip(capacity,rocks)])
        ret=0
        for n in needs:
            if n<=additionalRocks:
                ret+=1
                additionalRocks-=n
            else:
                break
        return ret


# @lc code=end


#
# @lcpr case=start
# [2,3,4,5]\n[1,2,4,4]\n2\n
# @lcpr case=end

# @lcpr case=start
# [10,2,2]\n[2,2,0]\n100\n
# @lcpr case=end

#
