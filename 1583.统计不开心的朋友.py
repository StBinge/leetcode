#
# @lc app=leetcode.cn id=1583 lang=python3
#
# [1583] 统计不开心的朋友
#
from sbw import *
# @lc code=start
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        ranks=[[0]*n for _ in range(n)]
        for i,prefer in enumerate(preferences):
            rank=n-1
            for j in prefer:
                ranks[i][j]=rank
                rank-=1

        ret=0
        friends=[-1]*n
        for x,y in pairs:
            friends[x]=y
            friends[y]=x

        for x in range(n):
            y=friends[x]
            for u in preferences[x]:
                if u==y:
                    break
                v=friends[u]    
                if ranks[u][v]<ranks[u][x]:
                    ret+=1
                    break
        return ret
# @lc code=end
assert Solution().unhappyFriends(n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]])==4
assert Solution().unhappyFriends(n = 2, preferences = [[1], [0]], pairs = [[1, 0]])==0
assert Solution().unhappyFriends(n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]])==2
