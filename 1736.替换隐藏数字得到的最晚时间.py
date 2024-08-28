#
# @lc app=leetcode.cn id=1736 lang=python3
#
# [1736] 替换隐藏数字得到的最晚时间
#
from sbw import *


# @lc code=start
class Solution:
    def maximumTime(self, time: str) -> str:
        ret=list(time)
        if ret[0]=='?':
            ret[0]='2' if time[1] == '?' or int(time[1])<4 else '1'
        
        if ret[1]=='?':
            ret[1]='3' if ret[0]=='2' else '9'
        
        if ret[3]=='?':
            ret[3]='5'
        
        if ret[4]=='?':
            ret[4]='9'
        return ''.join(ret)


# @lc code=end
assert Solution().maximumTime("??:3?") == "23:39"
assert Solution().maximumTime("0?:3?") == "09:39"
assert Solution().maximumTime("2?:?0") == "23:50"
