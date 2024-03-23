#
# @lc app=leetcode.cn id=1323 lang=python3
#
# [1323] 6 和 9 组成的最大数字
#

# @lc code=start
class Solution:
    def maximum69Number (self, num: int) -> int:
        digits=[]
        while num:
            digits.append(num%10)
            num//=10
        fliped=False
        ret=0
        for d in reversed(digits):
            if d==6 and not fliped:
                ret=ret*10+9
                fliped=True
            else:
                ret=ret*10+d
        return ret
# @lc code=end
assert Solution().maximum69Number(9669)==9969
