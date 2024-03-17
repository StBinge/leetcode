#
# @lc app=leetcode.cn id=1423 lang=python3
#
# [1423] 可获得的最大点数
#
from sbw import *
# @lc code=start
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k==1:
            return max(cardPoints[0],cardPoints[-1])
        tot=sum(cardPoints)
        L=len(cardPoints)
        remains=L-k
        if remains==0:
            return tot
        
        ret=cur=sum(cardPoints[:remains])
        for i in range(remains,L):
            cur+=cardPoints[i]-cardPoints[i-remains]
            ret=min(ret,cur)
        return tot-ret
# @lc code=end
assert Solution().maxScore(cardPoints = [1,1000,1], k = 1)==1
assert Solution().maxScore(cardPoints = [9,7,7,9,7,7,9], k = 7)==55
assert Solution().maxScore(cardPoints = [2,2,2], k = 2)==4
assert Solution().maxScore(cardPoints = [1,2,3,4,5,6,1], k = 3)==12
