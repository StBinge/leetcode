#
# @lc app=leetcode.cn id=2432 lang=python3
# @lcpr version=30204
#
# [2432] 处理用时最长的那个任务的员工
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        mx=0
        ret=0
        start=0
        for id,end in logs:
            time=end-start
            if time>mx:
                mx=time
                ret=id
            elif time==mx:
                ret=min(ret,id)
            start=end
        return ret
# @lc code=end



#
# @lcpr case=start
# 10\n[[0,3],[2,5],[0,9],[1,15]]\n
# @lcpr case=end

# @lcpr case=start
# 26\n[[1,1],[3,7],[2,12],[7,17]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[0,10],[1,20]]\n
# @lcpr case=end

#

