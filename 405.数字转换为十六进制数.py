#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
       
        if num<0:
            num=2**32+num
        digits='0123456789abcdef'
        ret=[]
        while num>0:
            n=num&0b1111
            ret.append(digits[n])
            num>>=4
        return ''.join(reversed(ret)) or '0'
# @lc code=end
assert Solution().toHex(26)=='1a'
assert Solution().toHex(-1)=='ffffffff'
assert Solution().toHex(-2)=='fffffffe'
assert Solution().toHex(0)=='0'
