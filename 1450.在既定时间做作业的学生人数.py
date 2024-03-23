#
# @lc app=leetcode.cn id=1450 lang=python3
#
# [1450] 在既定时间做作业的学生人数
#
from sbw import *
# @lc code=start
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ret=0
        for s,e in zip(startTime,endTime):
            if s>queryTime or e<queryTime:
                continue
            ret+=1
        return ret
# @lc code=end
assert Solution().busyStudent(startTime = [1,2,3], endTime = [3,2,7], queryTime = 4)==1
