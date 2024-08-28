#
# @lc app=leetcode.cn id=1986 lang=python3
# @lcpr version=30204
#
# [1986] 完成任务的最少工作时间段
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        def add(stamp,h):
            sessions,hours=stamp
            if hours+h>sessionTime:
                return [sessions+1,h]
            return [sessions,hours+h]

        N=len(tasks)
        f=[[float('inf')]*2]*(1<<N)
        f[0]=[0,0]
        for mask in range(1,1<<N):
            for i in range(N):
                if (1<<i) & mask:
                    f[mask]=min(f[mask],add(f[mask ^ (1<<i)],tasks[i]))
        s,h=f[-1]
        s+=h>0
        return s
        
                    

# @lc code=end
assert Solution().minSessions([7,4,3,8,10],12)==3
assert Solution().minSessions(tasks = [1,2,3], sessionTime = 3)==2


#
# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [3,1,3,1,1]\n8\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n15\n
# @lcpr case=end

#

