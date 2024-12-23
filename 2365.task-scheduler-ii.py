#
# @lc app=leetcode.cn id=2365 lang=python3
# @lcpr version=30204
#
# [2365] 任务调度器 II
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        ret=0
        pre_time={}
        for t in tasks:
            pre=pre_time.get(t,-1)
            if pre<0:
                ret+=1
                pre_time[t]=ret
            else:
                ret=max(ret+1,pre+space+1)
                pre_time[t]=ret
        return ret
# @lc code=end



#
# @lcpr case=start
# [1,2,1,2,3,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [5,8,8,5]\n2\n
# @lcpr case=end

#

