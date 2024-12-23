#
# @lc app=leetcode.cn id=2280 lang=python3
# @lcpr version=30204
#
# [2280] 表示一个折线图的最少线段数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices)==1:
            return 0
        stockPrices.sort()
        ret=0
        # day0,day1=stockPrices[:2]
        dy,dx=10**10,0
        for (x1,y1),(x2,y2) in pairwise(stockPrices):
            _dx,_dy=x2-x1,y2-y1
            if dx*_dy!=dy*_dx:
                ret+=1
                dx,dy=_dx,_dy
        return ret

# @lc code=end
assert Solution().minimumLines([[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]])==3
assert Solution().minimumLines([[3,4],[1,2],[7,8],[2,3]])==1


#
# @lcpr case=start
# [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,4],[1,2],[7,8],[2,3]]\n
# @lcpr case=end

#

