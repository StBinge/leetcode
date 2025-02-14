#
# @lc app=leetcode.cn id=2400 lang=python3
# @lcpr version=30204
#
# [2400] 恰好移动 k 步到达某一位置的方法数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        if startPos>endPos:
            startPos,endPos=endPos,startPos
        dif=endPos-startPos
        if dif>k or (k-dif)&1:
            return 0
        t=(k-dif)//2
        return math.comb(k,t)%(10**9+7)


# @lc code=end
assert Solution().numberOfWays(1,2,3)==3


#
# @lcpr case=start
# 1\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# 2\n5\n10\n
# @lcpr case=end

#

