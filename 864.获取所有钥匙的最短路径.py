#
# @lc app=leetcode.cn id=864 lang=python3
#
# [864] 获取所有钥匙的最短路径
#
from typing import List
# @lc code=start
from collections import deque
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        key_idx={}
        sr,sc=-1,-1
        R,C=len(grid),len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c]=='@':
                    sr,sc=r,c
                elif grid[r][c].islower():
                    if grid[r][c] not in key_idx:
                        key_idx[grid[r][c]]=len(key_idx)

        q=deque([(sr,sc,0)])
        dis={q[0]:0}
        target=(1<<(len(key_idx)))-1
        while q:
            r,c,mask=q.popleft()
            step=dis[(r,c,mask)]
            dirs=[-1,0,1,0,-1]
            for i in range(4):
                nr,nc=r+dirs[i],c+dirs[i+1]
                if nr<0 or nr==R or nc<0 or nc==C:
                    continue
                char=grid[nr][nc]
                if char=='#':
                    continue
                elif char.islower():
                    idx=key_idx[char]
                    nmask=mask|(1<<idx)
                    if nmask==target:
                        return step+1
                    if (nr,nc,nmask) in dis:
                        continue
                    dis[(nr,nc,nmask)]=step+1
                    q.append((nr,nc,nmask))
                elif char.isupper():
                    idx=key_idx[char.lower()]
                    if mask & (1<<idx)==0 or (nr,nc,mask) in dis:
                        continue
                    dis[(nr,nc,mask)]=step+1
                    q.append((nr,nc,mask))
                else:
                    if (nr,nc,mask) in dis:
                        continue
                    dis[(nr,nc,mask)]=step+1
                    q.append((nr,nc,mask))
        return -1
# @lc code=end
grid = ["@Aa"]
assert Solution().shortestPathAllKeys(grid)==-1

grid = ["@..aA","..B#.","....b"]
assert Solution().shortestPathAllKeys(grid)==6

grid = ["@.a.#","###.#","b.A.B"]
assert Solution().shortestPathAllKeys(grid)==8