#
# @lc app=leetcode.cn id=1185 lang=python3
#
# [1185] 一周中的第几天
#

# @lc code=start
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # 1971-1-1 => friday
        days=0
        days+=(year-1971)*365
        y=1972
        while y<year:
            days+=1
            y+=4

        months=[0,31,28,31,30,31,30,31,31,30,31,30,31
        ]
        days+=sum(months[:month])
        if month>2 and year % 4==0 and year !=2100:
            days+=1
        days+=day-1
        days%=7
        week=["Friday", "Saturday","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        return week[days]
    
# @lc code=end

assert Solution().dayOfTheWeek(day = 15, month = 8, year = 1993)=='Sunday'
assert Solution().dayOfTheWeek(day = 18, month = 7, year = 1999)=='Sunday'
assert Solution().dayOfTheWeek(day = 31, month = 8, year = 2019)=='Saturday'