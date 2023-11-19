#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x0=num
        while True:
            x1=(x0+num/x0)/2
            if x0-x1<10e-6:
                break
            x0=x1
        return int(x0)**2==num
    

# @lc code=end

assert Solution().isPerfectSquare(16)
assert Solution().isPerfectSquare(9)
assert Solution().isPerfectSquare(14)==False