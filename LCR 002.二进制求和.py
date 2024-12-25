#
# @lc app=leetcode.cn id=LCR 002 lang=python3
# @lcpr version=30204
#
# [LCR 002] 二进制求和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ret=[]
        carray=0
        for b1,b2 in zip_longest(reversed(a),reversed(b),fillvalue='0'):
            s=carray+int(b1)+int(b2)
            carray,s=divmod(s,2)
            ret.append(str(s))
        if carray:
            ret.append('1')
        return ''.join(reversed(ret))
# @lc code=end
assert Solution().addBinary('1111','1111')=='11110'
assert Solution().addBinary('11','10')=='101'


#
# @lcpr case=start
# "11"\n"10"\n
# @lcpr case=end

# @lcpr case=start
# "1010"\n"1011"\n
# @lcpr case=end

#

