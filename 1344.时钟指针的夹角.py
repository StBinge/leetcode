#
# @lc app=leetcode.cn id=1344 lang=python3
#
# [1344] 时钟指针的夹角
#

# @lc code=start
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
         min_angle=minutes*6
         hour%=12
         hour_angle=(hour+minutes/60)*30
         angle=abs(hour_angle-min_angle)
         return min(angle,360-angle)
# @lc code=end
assert Solution().angleClock(12,0)==0
assert Solution().angleClock(4,50)==155
assert Solution().angleClock(3,15)==7.5
assert Solution().angleClock(3,30)==75
assert Solution().angleClock(12,30)==165
