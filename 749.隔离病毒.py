#
# @lc app=leetcode.cn id=749 lang=python3
#
# [749] 隔离病毒
#
from typing import List
# @lc code=start
from collections import deque
import heapq
class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        R=len(isInfected)
        C=len(isInfected[0])
        dirs=[-1,0,1,0,-1]

       

        ret=0
        while True:
            neibours=[]
            firewalls=[]
            # idx=-1
            for x in range(R):
                for y in range(C):
                    if isInfected[x][y]==1:
                        idx=len(neibours)+1
                        queue=[[x,y]]
                        idx=-idx
                        isInfected[x][y]=idx
                        firewall=0
                        neighbour=set()
                        while queue:
                            r,c=queue.pop()
                            for i in range(4):
                                nr,nc=r+dirs[i],c+dirs[i+1]
                                if nr<0 or nr==R or nc<0 or nc==C:
                                    continue
                                if isInfected[nr][nc]==1:
                                    queue.append([nr,nc])
                                    isInfected[nr][nc]=idx
                                elif isInfected[nr][nc]==0:
                                    firewall+=1
                                    neighbour.add((nr,nc))
                        neibours.append(neighbour)
                        firewalls.append(firewall)
                    
            if len(neibours)==0:
                break
            if len(neibours)==1:
                ret+=firewalls[0]
                break
            idx=0
            Max=len(neibours[0])
            for nei in range(1,len(neibours)):
                if (n:=len(neibours[nei]))>Max:
                    idx=nei
                    Max=n
            ret+=firewalls[idx]
            tid=-idx-1
            for r in range(R):
                for c in range(C):
                    if isInfected[r][c]<0:
                        if isInfected[r][c]==tid:
                            isInfected[r][c]=2
                        else:
                            isInfected[r][c]=1
            
            for ii,nei in enumerate(neibours):
                if ii==idx:
                    continue
                for r,c in nei:
                    isInfected[r][c]=1
    

        return ret
# @lc code=end
isInfected=[[1,1,1],[1,0,1],[1,1,1]]
assert Solution().containVirus(isInfected)==4

isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
assert Solution().containVirus(isInfected)==10