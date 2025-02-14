#
# @lc app=leetcode.cn id=2712 lang=python3
# @lcpr version=30204
#
# [2712] 使所有字符相等的最小成本
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumCost(self, s: str) -> int:
        N=len(s)
        return sum(min(i,N-i) for i,(x,y) in enumerate(pairwise(s),1) if x!=y)
# @lc code=end
assert Solution().minimumCost('010101')==9
assert Solution().minimumCost('0011')==2


#
# @lcpr case=start
# "0011"\n
# @lcpr case=end

# @lcpr case=start
# "010101"\n
# @lcpr case=end

#

