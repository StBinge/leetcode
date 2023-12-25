#
# @lc app=leetcode.cn id=1007 lang=python3
#
# [1007] 行相等的最少多米诺旋转
#
from sbw import *
# @lc code=start
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        L=len(tops)
        ret=L+1
        up=[0]*7
        down=[0]*7
        total=[L]*7
        for t,b in zip(tops,bottoms):
            if t==b:
                total[t]-=1
                continue
            up[t]+=1
            down[b]+=1
        for x in range(1,7):
            if up[x]+down[x]<total[x]:
                continue
            ret=min(ret,min(up[x],down[x]))
        return ret if ret!=L+1 else -1
                
# @lc code=end
tops = [1,1,1,1,1,1,1,1]
bottoms = [1,1,1,1,1,1,1,1]
assert Solution().minDominoRotations(tops,bottoms)==0

tops = [3,5,1,2,3]
bottoms = [3,6,3,3,4]
assert Solution().minDominoRotations(tops,bottoms)==-1

tops = [2,1,2,4,2,2]
bottoms = [5,2,6,2,3,2]
assert Solution().minDominoRotations(tops,bottoms)==2
