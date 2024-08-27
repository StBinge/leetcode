#
# @lc app=leetcode.cn id=1735 lang=python3
#
# [1735] 生成乘积数组的方案数
#
from sbw import *
# @lc code=start
class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        N,M,Mod=10**4+14,14,10**9+7
        comb=[[0]*M for _ in range(N)]
        comb[0][0]=1
        for n in range(1,N):
            comb[n][0]=1
            for m in range(1,min(n+1,M)):
                comb[n][m]=(comb[n-1][m]+comb[n-1][m-1])%Mod
        lpf=[0]*N
        for i in range(2,N):
            if lpf[i]==0:
                for j in range(i,N,i):
                    if lpf[j]==0:
                        lpf[j]=i
        ret=[]
        for n,k in queries:
            ans=1
            while k>1:
                p=lpf[k]
                cnt=0
                while k%p==0:
                    cnt+=1
                    k//=p
                ans=(ans*comb[cnt+n-1][cnt])%Mod
            ret.append(ans)
        return ret
# @lc code=end
assert Solution().waysToFillArray([[373,196],[101,229],[466,109],[308,83],[296,432]])==[865201973,101,466,308,411805778]
assert Solution().waysToFillArray([[2,6],[5,1],[73,660]])==[4,1,50734910]
