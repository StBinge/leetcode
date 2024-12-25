#
# @lc app=leetcode.cn id=2374 lang=python3
# @lcpr version=30204
#
# [2374] 边积分最高的节点
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        N=len(edges)
        score=[0]*N
        for i,n in enumerate(edges):
            score[n]+=i
        ret=-1
        mx=0
        for i,s in enumerate(score):
            if s>mx:
                mx=s
                ret=i
        return ret
# @lc code=end



#
# @lcpr case=start
# [1,0,0,0,0,7,7,5]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,0,2]\n
# @lcpr case=end

#

