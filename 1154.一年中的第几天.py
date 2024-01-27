#
# @lc app=leetcode.cn id=1154 lang=python3
#
# [1154] 一年中的第几天
#

# @lc code=start
class Solution:
    def dayOfYear(self, date: str) -> int:
        parts=date.split('-')
        year=int(parts[0])
        month=int(parts[1])
        day=int(parts[2])
        offset=0
        if (year%4==0 and year%100!=0) or year % 400==0:
            offset=1
        ret=day
        # presums=[0,31,59,]
        while month>1:
            month-=1
            if month==2:
                ret+=28+offset
            elif month in [1,3,5,7,8,10,12]:
                ret+=31
            else:
                ret+=30
        return ret
# @lc code=end
assert Solution().dayOfYear("2019-01-09")==9
assert Solution().dayOfYear("2019-02-10")==41
