#
# @lc app=leetcode.cn id=3112 lang=python3
# @lcpr version=30204
#
# [3112] 访问消失节点的最少时间
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumTime(
        self, n: int, edges: List[List[int]], disappear: List[int]
    ) -> List[int]:
        adj = defaultdict(dict)
        for x, y, t in edges:
            paths = adj[x]
            if paths.get(y, float("inf")) <= t:
                continue
            adj[x][y] = t
            adj[y][x] = t

        ret = [float("inf")] * n
        ret[0] = 0
        q = [[0, 0]]
        while q:
            time, cur = heapq.heappop(q)
            if time > ret[cur]:
                continue
            for nxt, t in list(adj[cur].items()):
                if time + t >= disappear[nxt] or time + t >= ret[nxt]:
                    continue
                ret[nxt] = time + t
                heapq.heappush(q, [time + t, nxt])
        return [t if t < float("inf") else -1 for t in ret]


# @lc code=end
assert Solution().minimumTime(n=2, edges=[[0, 1, 1]], disappear=[1, 1]) == [0, -1]
assert Solution().minimumTime(
    n=3, edges=[[0, 1, 2], [1, 2, 1], [0, 2, 4]], disappear=[1, 3, 5]
) == [0, 2, 3]
assert Solution().minimumTime(
    n=3, edges=[[0, 1, 2], [1, 2, 1], [0, 2, 4]], disappear=[1, 1, 5]
) == [0, -1, 4]


#
# @lcpr case=start
# 3\n[[0,1,2],[1,2,1],[0,2,4]]\n[1,1,5]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[0,1,2],[1,2,1],[0,2,4]]\n[1,3,5]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[0,1,1]]\n[1,1]\n
# @lcpr case=end

#
