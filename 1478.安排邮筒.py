#
# @lc app=leetcode.cn id=1478 lang=python3
#
# [1478] 安排邮筒
#
from sbw import *
# @lc code=start
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        H=len(houses)
        if k>=H:
            return 0
        Max=float('inf')
        houses.sort()
        # preums=[0]
        # for dis in houses:
        #     preums.append(preums[-1]+dis)
        cost=[[0] * H for _ in range(H)]
        for i in range(H-2,-1,-1):
            cost[i][i+1]=houses[i+1]-houses[i]
            for j in range(i+2,H):
                cost[i][j]=cost[i+1][j-1]+houses[j]-houses[i]
        # def get_dis(x,y):
        #     ret=0
        #     while x<y:
        #         ret+=houses[y]-houses[x]
        #         x+=1
        #         y-=1
        #     return ret
        # f=[[Max]*(H+1) for _ in range(k)]
        f=[[Max]*H for _ in range(k)]
        for i in range(H):
            f[0][i]=cost[0][i]

        for i in range(1,k):
            for j in range(H):
                if i>=j:
                    f[i][j]=0
                    continue
                for p in range(j):
                    f[i][j]=min(f[i][j],f[i-1][p]+cost[p+1][j])
        return f[-1][-1]

# @lc code=end
assert Solution().minDistance([179,161,149,13,232,249,251,147,53,87,43,9,268,207,217,96,163,137,288,269,66,244,282,255,110,44,126,183,294,250,168,173,176,19,195,4,150]
,12)==152
assert Solution().minDistance(houses = [7,4,6,1], k = 1)==8
assert Solution().minDistance([1,8,12,10,3],3)==4
assert Solution().minDistance(houses = [3,6,14,10], k = 4)==0
assert Solution().minDistance(houses = [2,3,5,12,18], k = 2)==9
assert Solution().minDistance(houses = [1,4,8,10,20], k = 3)==5
