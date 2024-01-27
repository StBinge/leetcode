#
# @lc app=leetcode.cn id=1253 lang=python3
#
# [1253] 重构 2 行二进制矩阵
#
from sbw import *
# @lc code=start
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        s=0
        cnt2=0
        for col in colsum:
            s+=col
            cnt2+=col==2
        if sum(colsum)!=upper+lower or min(upper,lower)<cnt2:
            return []
        ret=[[],[]]
        for col in colsum:
            if col==0:
                ret[0].append(0)
                ret[1].append(0)
            elif col==2:
                ret[0].append(1)
                ret[1].append(1)
            elif upper>lower:
                ret[0].append(1)
                ret[1].append(0)
                upper-=1
            else:
                ret[0].append(0)
                ret[1].append(1)
                lower-=1
        return ret
    
# @lc code=end
assert Solution().reconstructMatrix(upper = 9, lower = 2, colsum = [0,1,2,0,0,0,0,0,2,1,2,1,2])==[]


upper = 5
lower = 5
colsum = [2,1,2,0,1,0,1,2,0,1]
ret=Solution().reconstructMatrix(upper,lower,colsum)
assert sum(ret[0])==upper and sum(ret[1])==lower and [a+b for a,b in zip(*ret)]==colsum

assert Solution().reconstructMatrix(upper = 2, lower = 3, colsum = [2,2,1,1])==[]
upper = 2
lower = 1
colsum = [1,1,1]
ret=Solution().reconstructMatrix(upper,lower,colsum)
assert sum(ret[0])==upper and sum(ret[1])==lower and [a+b for a,b in zip(*ret)]==colsum
