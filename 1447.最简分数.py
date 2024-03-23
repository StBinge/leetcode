#
# @lc app=leetcode.cn id=1447 lang=python3
#
# [1447] 最简分数
#
from sbw import *
# @lc code=start
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        vis=set()
        ret=[]
        for i in range(1,n):
            for j in range(i+1,n+1):
                if (i,j) in vis:
                    continue
                ret.append(f'{i}/{j}')
                k=2
                while k*j<=n:
                    vis.add((i*k,j*k))
                    k+=1
        return ret
# @lc code=end
assert sorted(Solution().simplifiedFractions(1))==sorted([])
assert sorted(Solution().simplifiedFractions(4))==sorted(["1/2","1/3","1/4","2/3","3/4"])
assert sorted(Solution().simplifiedFractions(3))==sorted(["1/2","1/3","2/3"])
assert sorted(Solution().simplifiedFractions(2))==sorted(["1/2"])
