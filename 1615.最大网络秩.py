#
# @lc app=leetcode.cn id=1615 lang=python3
#
# [1615] 最大网络秩
#
from sbw import *
# @lc code=start
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        indeg=[0]*n
        connect=[[False]*n for _ in range(n)]
        for x,y in roads:
            indeg[x]+=1
            indeg[y]+=1
            connect[x][y]=connect[y][x]=True
        first=[]
        second=[]
        s1=-1
        s2=-2
        for i,v in enumerate(indeg):
            if v>s1:
                second=first
                s2=s1
                s1=v
                first=[i]
            elif v==s1:
                first.append(i)
            elif v>s2:
                second=[i]
                s2=v
            elif v==s2:
                second.append(i)
        if len(first)==1:
            i=first[0]
            for j in second:
                if connect[i][j]==False:
                    return s1+s2
            return s1+s2-1
        else:
            L=len(first)
            if L*(L-1)//2>len(roads):
                return 2*s1
            for i in first:
                for j in first:
                    if i!=j and connect[i][j]==False:
                        return s1*2
            return s1*2-1

# @lc code=end
assert Solution().maximalNetworkRank(n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]])==5
assert Solution().maximalNetworkRank(n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]])==5
assert Solution().maximalNetworkRank(n = 4, roads = [[0,1],[0,3],[1,2],[1,3]])==4
