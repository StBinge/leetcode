#
# @lc app=leetcode.cn id=3342 lang=python3
# @lcpr version=30204
#
# [3342] 到达最后一个房间的最少时间 II
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        R,C=len(moveTime),len(moveTime[0])

        times=[[float('inf')]*C for _ in range(R)]
        q=[[0,0,0]]
        times[0][0]=0
        while q:
            t,x,y=heapq.heappop(q)
            if x==R-1 and y==C-1:
                return t
            if t>times[x][y]:
                continue
            dirs=[-1,0,1,0,-1]
            for i in range(4):
                nx,ny=x+dirs[i],y+dirs[i+1]
                if 0<=nx<R and 0<=ny<C:
                    _t=max(t,moveTime[nx][ny])+1+(x+y)%2
                    if _t<times[nx][ny]:
                        times[nx][ny]=_t
                        heapq.heappush(q,[_t,nx,ny])
# @lc code=end
assert Solution().minTimeToReach([[0,58],[27,69]])==71


#
# @lcpr case=start
# [[0,4],[4,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0,0,0],[0,0,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[1,2]]\n
# @lcpr case=end

#

