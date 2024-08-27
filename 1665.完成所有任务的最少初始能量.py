#
# @lc app=leetcode.cn id=1665 lang=python3
#
# [1665] 完成所有任务的最少初始能量
#
from sbw import *
# @lc code=start
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:x[1]-x[0])
        ret=0
        for cost,req in tasks:
            ret=max(ret+cost,req)
        return ret

# @lc code=end
assert Solution().minimumEffort([[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]])==27
assert Solution().minimumEffort([[1,3],[2,4],[10,11],[10,12],[8,9]])==32
assert Solution().minimumEffort([[1,2],[2,4],[4,8]])==8
