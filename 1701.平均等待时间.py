#
# @lc app=leetcode.cn id=1701 lang=python3
#
# [1701] 平均等待时间
#
from sbw import *
# @lc code=start
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait_time=0
        time=0
        for t1,t2 in customers:
            if t1>=time:
                time=t1+t2
            else:
                time+=t2
            wait_time+=time-t1
        return wait_time/len(customers)
# @lc code=end
assert abs(Solution().averageWaitingTime([[5,2],[5,4],[10,3],[20,1]])-3.25)<1e-5
assert abs(Solution().averageWaitingTime([[5,2],[5,4],[10,3],[20,1]])-3.25)<1e-5
assert abs(Solution().averageWaitingTime(customers = [[1,2],[2,5],[4,3]])-5.0)<1e-5
