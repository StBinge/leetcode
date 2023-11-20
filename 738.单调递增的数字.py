#
# @lc app=leetcode.cn id=738 lang=python3
#
# [738] 单调递增的数字
#

# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        N=n
        digits=[]
        nine_cnt=0
        while n>0:
            d=n%10
            if len(digits) and d>digits[-1]:
                nine_cnt=len(digits)
                d-=1
            digits.append(d)
            n//=10
        if nine_cnt==0:
            return N
        ret=0
        for d in reversed(digits[nine_cnt:]):
            ret=ret*10+d
        for i in range(nine_cnt):
            ret=ret*10+9
        return ret

                
# @lc code=end
assert Solution().monotoneIncreasingDigits(332)==299

assert Solution().monotoneIncreasingDigits(1234)==1234
assert Solution().monotoneIncreasingDigits(100)==99
assert Solution().monotoneIncreasingDigits(10)==9