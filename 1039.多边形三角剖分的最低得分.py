#
# @lc app=leetcode.cn id=1039 lang=python3
#
# [1039] 多边形三角剖分的最低得分
#
from sbw import *
# @lc code=start
class LinkNode:
    def __init__(self,val:int,prev:'LinkNode'=None,next:'LinkNode'=None) -> None:
        self.val=val
        self.prev=prev
        self.next=next
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def dp(i,j):
            if i+2>j:
                return 0
            if i+2==j:
                return values[i]*values[i+1]*values[i+2]
            
            return min(
                values[i]*values[j]*values[k]+dp(i,k)+dp(k,j) for k in range(i+1,j)
            )
        
        return dp(0,len(values)-1)

        

# @lc code=end
values = [1,3,1,4,1,5]
assert Solution().minScoreTriangulation(values)==13

values = [3,7,4,5]
assert Solution().minScoreTriangulation(values)==144

values = [1,2,3]
assert Solution().minScoreTriangulation(values)==6
