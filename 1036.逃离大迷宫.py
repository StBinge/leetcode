#
# @lc app=leetcode.cn id=1036 lang=python3
#
# [1036] 逃离大迷宫
#
from sbw import *
# @lc code=start
import heapq
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if len(blocked)<2:
            return True
        Boundary=10**6
        rows={source[0],target[0]}
        cols={source[1],target[1]}
        for r,c in blocked:
            rows.add(r)
            cols.add(c)
        rows=sorted(rows)
        cols=sorted(cols)
        rowid_map={}
        rid=0 if rows[0]==0 else 1
        rowid_map[rows[0]]=rid
        for i in range(1,len(rows)):
            if rows[i]==rows[i-1]+1:
                rid+=1
            else:
                rid+=2
            rowid_map[rows[i]]=rid
        
        if rows[-1]!=Boundary-1:
            rid+=2
        else:
            rid+=1


        colid_map={}
        cid=0 if cols[0]==0 else 1
        colid_map[cols[0]]=cid
        for i in range(1,len(cols)):
            if cols[i]==cols[i-1]+1:
                cid+=1
            else:
                cid+=2
            colid_map[cols[i]]=cid
        if cols[-1]!=Boundary-1:
            cid+=2
        else:
            cid+=1
        
        grid=[[0]*cid for _ in range(rid)]
        for r,c in blocked:
            grid[rowid_map[r]][colid_map[c]]=1
        
        sr,sc=rowid_map[source[0]],colid_map[source[1]]
        tr,tc=rowid_map[target[0]],colid_map[target[1]]

        q=deque([[sr,sc]])
        # vis=set()
        while q:
            r,c=q.popleft()
            # vis.add((r,c))
            dirs=[-1,0,1,0,-1]
            for i in range(4):
                nr,nc=r+dirs[i],c+dirs[i+1]
                if nr==tr and nc==tc:
                    return True
                if nr<0 or nr==rid or nc<0 or nc==cid or grid[nr][nc]==1:
                    continue
                q.append([nr,nc])
                grid[nr][nc]=1
        return False
        
# @lc code=end
blocked = []
source = [0,0]
target = [999999,999999]
assert Solution().isEscapePossible(blocked,source,target)

blocked = [[0,1],[1,0]]
source = [0,0]
target = [0,2]
assert not Solution().isEscapePossible(blocked,source,target)