#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        sum=1
        x=2
        while x*x<num:
            if num%x==0:
                sum+=x+num//x
            x+=1
        if x*x==num:
            sum+=x
        return sum==num
# @lc code=end
assert Solution().checkPerfectNumber(28)
assert Solution().checkPerfectNumber(7)==False
assert Solution().checkPerfectNumber(1)==False
