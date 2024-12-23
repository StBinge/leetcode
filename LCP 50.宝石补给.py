#
# @lc app=leetcode.cn id=LCP 50 lang=python3
# @lcpr version=30204
#
# [LCP 50] 宝石补给
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:        
        for x,y in operations:
            give=gem[x]//2
            gem[y]+=give
            gem[x]-=give
        return max(gem)-min(gem)
# @lc code=end



#
# @lcpr case=start
# [3,1,2]\n[[0,2],[2,1],[2,0]]`>\n
# @lcpr case=end

# @lcpr case=start
# [100,0,50,100]\n[[0,2],[0,1],[3,0],[3,0]]`>\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0,0]\n[[1,2],[3,1],[1,2]]`>\n
# @lcpr case=end

#

