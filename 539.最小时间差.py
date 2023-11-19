#
# @lc app=leetcode.cn id=539 lang=python3
#
# [539] 最小时间差
#
from typing import List
# @lc code=start
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        def parse(s:str):
            return int(s[:2])*60+int(s[3:])
        ret=24**60
        pre=parse(timePoints[-1])-24*60
        for i in range(len(timePoints)):
            
            cur=parse(timePoints[i])
            ret=min(ret,cur-pre)
            pre=cur
            if ret==0:
                break
        return ret
# @lc code=end

assert Solution().findMinDifference(["23:59","00:00"])==1
assert Solution().findMinDifference(["00:00","23:59","00:00"])==0