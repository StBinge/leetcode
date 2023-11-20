#
# @lc app=leetcode.cn id=838 lang=python3
#
# [838] 推多米诺
#

# @lc code=start
from collections import deque
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n=len(dominoes)
        force=[[] for _ in range(n)]
        time=[-1]*n
        queue=deque()
        for i,f in enumerate(dominoes):
            if f!='.':
                time[i]=0
                force[i].append(f)
                queue.append(i)
        
        ret=['.']*n
        while queue:
            i=queue.popleft()
            if len(force[i])==1:
                ret[i]=f=force[i][0]
                ni=i-1 if f=='L' else i+1
                t=time[i]
                if 0<=ni<n:
                    if time[ni]==-1:
                        time[ni]=t+1
                        force[ni].append(f)
                        queue.append(ni)
                    elif time[ni]==t+1:
                        force[ni].append(f)
        return ''.join(ret)


# @lc code=end
dominoes = ".L.R...LR..L.."
ret="LL.RR.LLRRLL.."
assert Solution().pushDominoes(dominoes)==ret

dominoes = "RR.L"
ret="RR.L"
assert Solution().pushDominoes(dominoes)==ret