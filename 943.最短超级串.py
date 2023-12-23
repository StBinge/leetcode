#
# @lc app=leetcode.cn id=943 lang=python3
#
# [943] 最短超级串
#
from sbw import *
# @lc code=start
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        L=len(words)
        overlaps=[[0]*L for _ in range(L)]
        for i,w1 in enumerate(words):
            for j,w2 in enumerate(words):
                if i==j:
                    continue
                for k in range(min(len(w1),len(w2)),-1,-1):
                    if w1.endswith(w2[:k]):
                        overlaps[i][j]=k
                        break
        
        f=[[0]*L for _ in range(1<<L)]
        p=[[-1]*L for _ in range(1<<L)]

        for mask in range(1,1<<L):
            for bit in range(L):
                if mask & 1<<bit ==0:
                    continue
                p_mask=mask ^ 1<<bit
                if p_mask==0:
                    continue
                value=0
                for i in range(L):
                    if p_mask & 1<<i==0:
                        continue
                    value=max(value,f[p_mask][i]+overlaps[i][bit])
                    if value>f[mask][bit]:
                        f[mask][bit]=value
                        p[mask][bit]=i
        
        path=[]
        i=max(range(L),key=f[-1].__getitem__)
        seen=[False]*L
        while i>=0:
            path.append(i)
            seen[i]=True
            mask,i=mask ^ 1<<i,p[mask][i]
        path.reverse()
        for i in range(L):
            if not seen[i]:
                path.append(i)

        ret=[words[path[0]]]
        for i in range(1,len(path)):
            # word_idx=path[i]
            overlap=overlaps[path[i-1]][path[i]]
            ret.extend(words[path[i]][overlap:])

        return ''.join(ret)
# @lc code=end
words = ["catg","ctaagt","gcta","ttca","atgcatc"]
ret="gctaagttcatgcatc"
ans= Solution().shortestSuperstring(words)
assert len(ans)==len(ret)

words = ["alex","loves","leetcode"]
ret="alexlovesleetcode"
ans= Solution().shortestSuperstring(words)
assert len(ans)==len(ret)