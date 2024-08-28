#
# @lc app=leetcode.cn id=1844 lang=python3
#
# [1844] 将所有数字用字符替换
#

# @lc code=start
class Solution:
    def replaceDigits(self, s: str) -> str:
        ret=list(s)
        N=len(s)
        for i in range(1,N,2):
            ret[i]=chr(ord(s[i-1])+ord(s[i])-ord('0'))
        return ''.join(ret)
# @lc code=end
assert Solution().replaceDigits('a1b2c3d4e')=='abbdcfdhe'
assert Solution().replaceDigits('a1c1e1')=='abcdef'
