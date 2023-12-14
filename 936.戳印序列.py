#
# @lc app=leetcode.cn id=936 lang=python3
#
# [936] 戳印序列
#
from sympy import Max, false
from sbw import *
# @lc code=start
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        ls=len(stamp)
        lt=len(target)
        edges=[[] for _ in range(lt)]
        indegree=[ls]*(lt-ls+1)
        ret=[]
        queue=[]
        flag=[False]*lt
        for i in range(lt-ls+1):
            for j in range(ls):
                if stamp[j]==target[i+j]:
                    indegree[i]-=1
                    if indegree[i]==0:
                        queue.append(i)
                else:
                    edges[i+j].append(i)
            
        while queue:
            k=queue.pop()
            ret.append(k)
            for i in range(ls):
                if flag[k+i]==False:
                    flag[k+i]=True
                    for edge in edges[k+i]:
                        indegree[edge]-=1
                        if indegree[edge]==0:
                            queue.append(edge)
        return ret[::-1] if len(ret)==lt-ls+1 else []

# @lc code=end
stamp = "mda"
target = "mdadddaaaa"
print(Solution().movesToStamp(stamp,target))

stamp = "abca"
target = "aabcaca"
print(Solution().movesToStamp(stamp,target))

stamp = "abc"
target = "ababc"
print(Solution().movesToStamp(stamp,target))
