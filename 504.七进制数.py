#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        neg=num<0
        if neg:
            num=-num
        ret=[]
        while num>0:
            ret.append(str(num%7))
            num//=7
        if neg:
            ret.append('-')
        return ''.join(reversed(ret)) or '0'
# @lc code=end
assert Solution().convertToBase7(0)=='0'
assert Solution().convertToBase7(100)=='202'
assert Solution().convertToBase7(-7)=='-10'
