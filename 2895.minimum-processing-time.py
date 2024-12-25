#
# @lc app=leetcode.cn id=2895 lang=python3
# @lcpr version=30204
#
# [2895] 最小处理时间
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        return max(p+t for p,t in zip(processorTime,tasks[3::4]))
# @lc code=end



#
# @lcpr case=start
# [8,10]\n[2,2,3,1,8,7,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [10,20]\n[2,3,1,2,5,8,4,3]\n
# @lcpr case=end

#

