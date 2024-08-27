#
# @lc app=leetcode.cn id=1817 lang=python3
#
# [1817] 查找用户活跃分钟数
#
from sbw import *
# @lc code=start
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        time_cnt=defaultdict(set)
        for id,t in logs:
            time_cnt[id].add(t)
        ret=[0]*k
        for times in time_cnt.values():
            ret[len(times)-1]+=1
        return ret
# @lc code=end
assert Solution().findingUsersActiveMinutes(logs = [[1,1],[2,2],[2,3]], k = 4)==[1,1,0,0]
assert Solution().findingUsersActiveMinutes(logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5)==[0,2,0,0,0]
