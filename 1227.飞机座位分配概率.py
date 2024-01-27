#
# @lc app=leetcode.cn id=1227 lang=python3
#
# [1227] 飞机座位分配概率
#

# @lc code=start
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 0.5 if n>1 else 1
# @lc code=end

assert Solution().nthPersonGetsNthSeat(3)==0.5
assert Solution().nthPersonGetsNthSeat(2)==0.5
assert Solution().nthPersonGetsNthSeat(1)==1