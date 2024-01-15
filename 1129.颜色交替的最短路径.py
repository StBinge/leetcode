#
# @lc app=leetcode.cn id=1129 lang=python3
#
# [1129] 颜色交替的最短路径
#
from sbw import *
# @lc code=start
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # [end_with_r,end_with_b]
        ret=[-1]*n
        # ret[0]=[0,0]
        reds={}
        for a,b in redEdges:
            reds.setdefault(a,[]).append(b)
        blues={}
        for u,v in blueEdges:
            blues.setdefault(u,[]).append(v)

        # 0:red
        # 1:blue
        queue=deque([[0,0,0],[0,0,1]])
        # step=0
        vis=[[False,False] for _ in range(n)]
        while queue:
            step,cur,mark=queue.popleft()
            vis[cur][mark]=True
            if ret[cur]<0:
                ret[cur]=step
            nxt_nodes=reds if mark==1 else blues
            if cur not in nxt_nodes:
                continue
            step+=1
            end_mark=1-mark
            for node in nxt_nodes[cur]:
                if not vis[node][end_mark]:
                    queue.append([step,node,end_mark])
        return ret
# @lc code=end
assert Solution().shortestAlternatingPaths(5,
[[0,1],[1,2],[2,3],[3,4]],
[[1,2],[2,3],[3,1]])==[0,1,2,3,7]
assert Solution().shortestAlternatingPaths(n = 3, redEdges= [[0,1]], blueEdges= [[2,1]])==[0,1,-1]
assert Solution().shortestAlternatingPaths(n = 3, redEdges= [[0,1],[1,2]], blueEdges= [])==[0,1,-1]
