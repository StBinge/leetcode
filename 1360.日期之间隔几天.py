#
# @lc app=leetcode.cn id=1360 lang=python3
#
# [1360] 日期之间隔几天
#

# @lc code=start
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        months=[31,28,31,30,31,30,31,31,30,31,30,31]
        def dif(s:str):
            year=int(s[:4])
            month=int(s[5:7])
            day=int(s[8:10])
            ret=(year-1971)*365
            ret+=sum(months[:month-1])
            ret+=day
            extra=(year-1968)//4
            if year % 4 ==0 and month<3:
                extra-=1
            if year==2100 and month>3:
                extra-=1
            ret+=extra
            return ret
        return abs(dif(date1)-dif(date2))

# @lc code=end
assert Solution().daysBetweenDates(date1 = "2020-01-15", date2 = "2019-12-31")==15
assert Solution().daysBetweenDates("2019-06-29", date2 = "2019-06-30")==1
