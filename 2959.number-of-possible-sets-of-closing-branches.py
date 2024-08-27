#
# @lc app=leetcode.cn id=2959 lang=python3
# @lcpr version=30204
#
# [2959] 关闭分部的可行集合数目
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        def floyd(nodes: list):
            N=len(nodes)
            f=[None]*N
            for i,n in enumerate(nodes):
                row=[]
                for nxt in nodes:
                    row.append(edges[n][nxt])
                row[i]=0
                f[i]=row
            
            for k in range(N):
                # kn=nodes[k]
                for i in range(N):
                    # i_n=nodes[i]
                    if f[k][i]>maxDistance:
                        continue
                    for j in range(N):
                        # jn=nodes[j]
                        f[i][j]=min(f[i][j],f[i][k]+f[k][j])
            for row in f:
                for d in row:
                    if d>maxDistance:
                        return 0
            return 1

        edges = [[10**6] * n for _ in range(n)]
        for x, y, w in roads:
            if w > maxDistance:
                continue
            if edges[x][y] > w:
                edges[x][y] = w
                edges[y][x] = w
        
        Mask = 1 << n
        ret = 1
        for mask in range(1, Mask):
            cnt = mask.bit_count()
            if cnt == 1:
                ret += 1
                continue
            nodes = deque()
            for i in range(n):
                if mask >> i & 1:
                    nodes.append(i)
            if cnt == 2:
                x = nodes.pop()
                y = nodes.pop()
                if edges[x][y] <= maxDistance:
                    ret += 1
                    # print(x,y)
                continue
            # dist=[maxDistance+1]*len(nodes)
            ret+=floyd(nodes)
        return ret


# @lc code=end
assert Solution().numberOfSets(5,25,[[1,0,17],[1,0,1],[2,1,24],[3,2,12],[1,0,7],[3,2,4],[2,1,15],[0,4,14]]) == 14
assert Solution().numberOfSets(4,17,[[2,1,28],[2,0,6],[1,0,28],[1,0,24],[1,0,18],[1,0,25],[0,3,10]]) == 8
assert Solution().numberOfSets(n=1, maxDistance=10, roads=[]) == 2
assert (
    Solution().numberOfSets(
        n=3, maxDistance=5, roads=[[0, 1, 20], [0, 1, 10], [1, 2, 2], [0, 2, 2]]
    )
    == 7
)
assert (
    Solution().numberOfSets(
        n=3, maxDistance=5, roads=[[0, 1, 2], [1, 2, 10], [0, 2, 10]]
    )
    == 5
)


#
# @lcpr case=start
# 3\n5\n[[0,1,2],[1,2,10],[0,2,10]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n5\n[[0,1,20],[0,1,10],[1,2,2],[0,2,2]]\n
# @lcpr case=end

# @lcpr case=start
# 1\n10\n[]\n
# @lcpr case=end

#
