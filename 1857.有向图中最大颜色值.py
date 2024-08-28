#
# @lc app=leetcode.cn id=1857 lang=python3
#
# [1857] 有向图中最大颜色值
#
from sbw import *


# @lc code=start
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        N = len(colors)
        indeg = [0] * N
        path = defaultdict(list)
        for a, b in edges:
            if a == b:
                return -1
            indeg[b] += 1
            path[a].append(b)

        q = deque()
        for i, d in enumerate(indeg):
            if d == 0:
                q.append(i)

        cnt = 0
        f=[[0]*26 for _ in range(N)]

        while q:
            node=q.popleft()
            cnt+=1
            code=ord(colors[node])-ord('a')
            f[node][code]+=1
            for nxt in path[node]:
                for i in range(26):
                    f[nxt][i]=max(f[nxt][i],f[node][i])
                indeg[nxt]-=1
                if indeg[nxt]==0:
                    q.append(nxt)
        if cnt!=N:
            return -1
        return max(max(l) for l in f)


# @lc code=end
assert Solution().largestPathValue("spppsssss",[[0,1],[1,2],[2,3],[0,4],[4,5],[4,6],[5,6],[6,7],[5,7],[1,8]]) == 5
assert Solution().largestPathValue(colors="a", edges=[[0, 0]]) == -1
assert (
    Solution().largestPathValue(colors="abaca", edges=[[0, 1], [0, 2], [2, 3], [3, 4]])
    == 3
)
