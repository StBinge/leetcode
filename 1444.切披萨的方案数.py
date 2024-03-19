#
# @lc app=leetcode.cn id=1444 lang=python3
#
# [1444] 切披萨的方案数
#
from sbw import *
# @lc code=start
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        R,C=len(pizza),len(pizza[0])
        f=[[0]*(C+1) for _ in range(R+1)]
        presums=[[0]*(C+1) for _ in range(R+1)]
        for r in range(R-1,-1,-1):
            for c in range(C-1,-1,-1):
                presums[r][c]=presums[r][c+1]+presums[r+1][c]+int(pizza[r][c]=='A')-presums[r+1][c+1]
                if presums[r][c]:
                    f[r][c]=1
        tot=presums[0][0]
        if tot<k:
            return 0

        # def get_apples(r1,c1,r2,c2):
        #     return presums[r2+1][c2+1]-presums[r2+1][c1]-presums[r1][c2+1]+presums[r1][c1]

        Mode=10**9+7
        for _ in range(k-1):
            cols=[0]*C
            for r in range(R-1,-1,-1):
                rows=0
                for c in range(C-1,-1,-1):
                    temp=f[r][c]
                    if presums[r][c]==presums[r+1][c]:
                        f[r][c]=f[r+1][c]
                    elif presums[r][c]==presums[r][c+1]:
                        f[r][c]=f[r][c+1]
                    else:
                        f[r][c]=(rows+cols[c])%Mode
                    rows+=temp
                    cols[c]+=temp
        return f[0][0]
# @lc code=end
assert Solution().ways(pizza = ["A..","AA.","..."], k = 3)==1
assert Solution().ways(pizza = ["A..","A..","..."], k = 1)==1
assert Solution().ways(pizza = ["A..","AAA","..."], k = 3)==3
