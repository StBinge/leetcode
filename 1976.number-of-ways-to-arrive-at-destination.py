#
# @lc app=leetcode.cn id=1976 lang=python3
# @lcpr version=30204
#
# [1976] 到达目的地的方案数
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mods = 10**9 + 7
        adj = [[] for _ in range(n)]
        for x, y, t in roads:
            adj[x].append([y, t])
            adj[y].append([x, t])


        heap = [[0, 0]]  # [cost,cur,prev]
        cost = [float("inf")] * n
        cost[0] = 0
        f=[0]*n
        f[0]=1
        while True:
            time, cur = heapq.heappop(heap)
            if cur==n-1:
                break
            for nxt, t in adj[cur]:
                _cost=t+time
                if _cost > cost[nxt]:
                    continue
                elif _cost==cost[nxt]:
                    f[nxt]+=f[cur]
                    f[nxt]%=mods
                else:
                    cost[nxt]=_cost
                    f[nxt]=f[cur]
                    heapq.heappush(heap, [time + t, nxt])
        return f[-1]


# @lc code=end
assert Solution().countPaths(12,[[1,0,2348],[2,1,2852],[2,0,5200],[3,1,12480],[2,3,9628],[4,3,7367],[4,0,22195],[5,4,5668],[1,5,25515],[0,5,27863],[6,5,836],[6,0,28699],[2,6,23499],[6,3,13871],[1,6,26351],[5,7,6229],[2,7,28892],[1,7,31744],[3,7,19264],[6,7,5393],[2,8,31998],[8,7,3106],[3,8,22370],[8,4,15003],[8,6,8499],[8,5,9335],[8,9,5258],[9,2,37256],[3,9,27628],[7,9,8364],[1,9,40108],[9,5,14593],[2,10,45922],[5,10,23259],[9,10,8666],[10,0,51122],[10,3,36294],[10,4,28927],[11,4,25190],[11,9,4929],[11,8,10187],[11,6,18686],[2,11,42185],[11,3,32557],[1,11,45037]])==166
assert Solution().countPaths(n = 2, roads = [[1,0,10]])==1
assert (
    Solution().countPaths(
        n=7,
        roads=[
            [0, 6, 7],
            [0, 1, 2],
            [1, 2, 3],
            [1, 3, 3],
            [6, 3, 3],
            [3, 5, 1],
            [6, 5, 1],
            [2, 5, 1],
            [0, 4, 5],
            [4, 6, 2],
        ],
    )
    == 4
)


#
# @lcpr case=start
# 7\n[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[1,0,10]]\n
# @lcpr case=end

#
