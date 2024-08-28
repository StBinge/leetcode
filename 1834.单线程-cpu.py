#
# @lc app=leetcode.cn id=1834 lang=python3
#
# [1834] 单线程 CPU
#
from sbw import *
# @lc code=start
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        N=len(tasks)
        sorted_indices=sorted(range(N),key=lambda x:tasks[x][0])
        ret=[]
        # end=sorted_tasks[0][1]
        time=0
        idx=0
        heap=[]
        r=0
        while len(ret)<N:
            while idx<N and tasks[sorted_indices[idx]][0]<=time:
                tid=sorted_indices[idx]
                end_time=tasks[tid][1]
                heapq.heappush(heap,[end_time,tid])
                idx+=1
            if not heap:
                time=tasks[sorted_indices[idx]][0]
            else:
                e,tid=heapq.heappop(heap)
                ret.append(tid)
                time+=e
        return ret
# @lc code=end
assert Solution().getOrder([[7,10],[7,12],[7,5],[7,4],[7,2]])==[4,3,2,0,1]
assert Solution().getOrder([[1,2],[2,4],[3,2],[4,1]])==[0,2,3,1]
