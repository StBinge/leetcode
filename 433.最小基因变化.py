#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#
from typing import List
# @lc code=start
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene==endGene:
            return 0

        def can_change(s1,s2):
            cnt=0
            for i in range(8):
                if s1[i]!=s2[i]:
                    cnt+=1
                    if cnt>1:
                        return False
            return cnt==1
        
        N=len(bank)
        edges=[[0]*N for _ in range(N)]
        end_idx=-1
        for i in range(N):
            s1=bank[i]
            if s1==endGene:
                end_idx=i
            for j in range(i+1,N):
                s2=bank[j]
                if can_change(s1,s2):
                    edges[i][j]=1
                    edges[j][i]=1
        if end_idx<0:
            return -1
        queue=[i for i in range(N) if can_change(startGene,bank[i])]
        step=0
        vis=set(queue)
        while queue:
            nxt=[]
            step+=1
            for i in queue:
                if i==end_idx:
                    return step
                for j in range(N):
                    if edges[i][j] and j not in vis:
                        nxt.append(j)
                        vis.add(j)
            queue=nxt
        return -1
# @lc code=end

start = "AACCGGTT"
end = "AACCGGTA"
bank = []
assert Solution().minMutation(start,end,bank)==-1

start = "AACCGGTT"
end = "AACCGGTA"
bank = ["AACCGGTA"]
assert Solution().minMutation(start,end,bank)==1
start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
assert Solution().minMutation(start,end,bank)==2

start = "AAAAACCC"
end = "AACCCCCC"
bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
assert Solution().minMutation(start,end,bank)==3