#
# @lc app=leetcode.cn id=1434 lang=python3
#
# [1434] 每个人戴不同帽子的方案数
#
from sbw import *
# @lc code=start
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        Mod=10**9+7
        hat_person={}
        for p,hat in enumerate(hats):
            for h in hat:
                hat_person.setdefault(h,[]).append(p)
        L=len(hats)
        # f=[[0]*(1<<L) for _ in range(41)]
        f0=[0]*(1<<L)
        f1=f0.copy()
        f0[0]=1
        for h in range(1,41):
            if h not in hat_person:
                continue
            for mask in range(1<<L):
                f1[mask]=f0[mask]
                for p in hat_person[h]:
                    if mask & (1<<p):
                        f1[mask]+=f0[mask ^ (1<<p)]
                f1[mask]%=Mod
            f0,f1=f1,f0
        return f0[-1]

# @lc code=end
assert Solution().numberWays([[1,2,4,6,7,8,9,11,12,13,14,15,16,18,19,20,23,24,25],[2,5,16],[1,4,5,6,7,8,9,12,15,16,17,19,21,22,24,25],[1,3,6,8,11,12,13,16,17,19,20,22,24,25],[11,12,14,16,18,24],[2,3,4,5,7,8,13,14,15,17,18,21,24],[1,2,6,7,10,11,13,14,16,18,19,21,23],[1,3,6,7,8,9,10,11,12,14,15,16,18,20,21,22,23,24,25],[2,3,4,6,7,10,12,14,15,16,17,21,22,23,24,25]]
)==778256459
assert Solution().numberWays([[1,2],[1,3],[2,3],[3]])==0
assert Solution().numberWays([[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]])==111
assert Solution().numberWays([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])==24
assert Solution().numberWays(hats = [[3,5,1],[3,5]])==4
assert Solution().numberWays(hats = [[3,4],[4,5],[5]])==1
