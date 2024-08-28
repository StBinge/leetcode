#
# @lc app=leetcode.cn id=1723 lang=python3
#
# [1723] 完成所有工作的最短时间
#
from sbw import *


# @lc code=start
import random
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:

        ret=float('inf')
        N=len(jobs)
        High=1e8
        Low=1e-4
        Fa=0.8
        def calc():
            works=[0]*k
            for i in range(N):
                w_idx,w_time=0,works[0]
                for j in range(k):
                    if works[j]<w_time:
                        w_idx=j
                        w_time=works[j]
                works[w_idx]+=jobs[i]
            _max= max(works)
            nonlocal ret
            ret=min(ret,_max)
            return _max
        def sa():
            random.shuffle(jobs)
            t=High
            while t>Low:
                a,b=randint(0,N-1),randint(0,N-1)
                prev=calc()
                jobs[a],jobs[b]=jobs[b],jobs[a]
                cur=calc()
                if cur>prev and math.log((cur-prev))/t>random.random():
                    jobs[a],jobs[b]=jobs[b],jobs[a]
                t=t*Fa

        for _ in range(100):
            sa()
        return ret


# @lc code=end
assert Solution().minimumTimeRequired(jobs = [5,5,4,4,4], k = 2) == 12
assert Solution().minimumTimeRequired(jobs = [1,2,4,7,8], k = 2) == 11
assert Solution().minimumTimeRequired(jobs=[3, 2, 3], k=3) == 3
