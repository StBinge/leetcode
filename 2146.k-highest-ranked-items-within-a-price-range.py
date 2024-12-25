#
# @lc app=leetcode.cn id=2146 lang=python3
# @lcpr version=30204
#
# [2146] 价格范围内最高排名的 K 样物品
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def highestRankedKItems(
        self, grid: List[List[int]], pricing: List[int], start: List[int], k: int
    ) -> List[List[int]]:
        lo, hi = pricing
        R, C = len(grid), len(grid[0])
        q=[start]
        vis=[[False]*C for _ in range(R)]
        vis[start[0]][start[1]]=True
        sort_key=lambda pos:[grid[pos[0]][pos[1]],pos]
        ret=[]
        while q:
            q.sort(key=sort_key)
            ret.extend([p for p in q if lo<=grid[p[0]][p[1]]<=hi])
            if len(ret)>=k:
                return ret[:k]
            nxt=[]
            for r,c in q:
                dirs = [-1, 0, 1, 0, -1]
                for i in range(4):
                    nr, nc = r + dirs[i], c + dirs[i + 1]
                    if 0<=nr<R and 0<=nc<C and grid[nr][nc]!=0 and vis[nr][nc]==False:
                        nxt.append([nr,nc])
                        vis[nr][nc]=True
            q=nxt
                    
        return ret


# @lc code=end
assert Solution().highestRankedKItems(
    grid=[[1, 2, 0, 1], [1, 3, 0, 1], [0, 2, 5, 1]], pricing=[2, 5], start=[0, 0], k=3
) == [[0, 1], [1, 1], [2, 1]]


#
# @lcpr case=start
# [[1,2,0,1],[1,3,0,1],[0,2,5,1]]\n[2,5]\n[0,0]\n3\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,0,1],[1,3,3,1],[0,2,5,1]]\n[2,3]\n[2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,1],[0,0,1],[2,3,4]]\n[2,3]\n[0,0]\n3\n
# @lcpr case=end

#
