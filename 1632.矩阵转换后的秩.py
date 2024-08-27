#
# @lc app=leetcode.cn id=1632 lang=python3
#
# [1632] 矩阵转换后的秩
#
from sbw import *
# @lc code=start
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        R,C=len(matrix),len(matrix[0])
        p=list(range(R*C))
        size=[1]*(R*C)
        def find(x):
            if p[x]!=x:
                p[x]=find(p[x])
            return p[x]

        def union(x,y):
            px,py=find(x),find(y)
            if px==py:
                return
            if size[px]<size[py]:
                px,py=py,px
            p[py]=px
            size[px]+=size[py]

        for r in range(R):
            v_idx=defaultdict(list)
            for c in range(C):
                v=matrix[r][c]
                v_idx[v].append(r*C+c)
            for indices in v_idx.values():
                root=indices[0]
                for nxt in indices[1:]:
                    union(root,nxt)
        for c in range(C):
            v_idx=defaultdict(list)
            for r in range(R):
                v=matrix[r][c]
                v_idx[v].append(r*C+c)
            for indices in v_idx.values():
                root=indices[0]
                for nxt in indices[1:]:
                    union(root,nxt)
        roots=[x for x in range(R*C) if x==p[x]]
        indegree=defaultdict(int)
        adj=defaultdict(list)
        for r in range(R):
            v_idx={}
            for c in range(C):
                v=matrix[r][c]
                v_idx[v]=r*C+c
            keys=sorted(v_idx.keys())
            for pre,nxt in pairwise(keys):
                px=find(v_idx[nxt])
                indegree[px]+=1
                py=find(v_idx[pre])
                adj[py].append(px)
        for c in range(C):
            v_idx={}
            for r in range(R):
                v_idx[matrix[r][c]]=r*C+c

            keys=sorted(v_idx.keys())
            for pre,nxt in pairwise(keys):
                px=find(v_idx[nxt])
                indegree[px]+=1
                py=find(v_idx[pre])
                adj[py].append(px)
        
        q=deque([[x,1] for x in roots if indegree[x]==0])
        ret=[[0]*C for _ in range(R)]
        ranks={}
        while q:
            idx,rk=q.popleft()
            ranks[idx]=rk
            for j in adj[idx]:
                indegree[j]-=1
                if indegree[j]==0:
                    q.append([j,rk+1])

        for idx in range(R*C):
            r,c=idx//C,idx%C
            ret[r][c]=ranks[find(idx)]
        return ret

# @lc code=end
assert Solution().matrixRankTransform([[-37,-50,-3,44],[-37,46,13,-32],[47,-42,-3,-40],[-17,-22,-39,24]])==[[2,1,4,6],[2,6,5,4],[5,2,4,3],[4,3,1,5]]
assert Solution().matrixRankTransform([[7,3,6],[1,4,5],[9,8,2]])==[[5,1,4],[1,2,3],[6,3,1]]
assert Solution().matrixRankTransform([[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]])==[[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
assert Solution().matrixRankTransform([[7,7],[7,7]])==[[1,1],[1,1]]
assert Solution().matrixRankTransform([[1,2],[3,4]])==[[1,2],[2,3]]
