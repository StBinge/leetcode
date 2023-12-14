#
# @lc app=leetcode.cn id=963 lang=python3
#
# [963] 最小面积矩形 II
#
from sbw import *
# @lc code=start
import math,itertools
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        points=[complex(*p) for p in points]
        seen={}
        for p,q in itertools.combinations(points,2):
            mid=(p+q)/2
            r=abs(p-mid)
            seen.setdefault((mid,r),[]).append(p)
        
        ret=float('inf')
        for (mid,r),canidates in seen.items():
            for p,q in itertools.combinations(canidates,2):
                ret=min(ret,abs(p-q)*abs(p-(2*mid-q)))


        
        return 0 if math.isinf(ret) else ret



# @lc code=end
assert Solution().minAreaFreeRect([[0,3],[1,2],[3,1],[1,3],[2,1]])==0
assert Solution().minAreaFreeRect([[0,1],[2,1],[1,1],[1,0],[2,0]])==1
assert Solution().minAreaFreeRect([[1,2],[2,1],[1,0],[0,1]])==2
