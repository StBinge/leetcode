#
# @lc app=leetcode.cn id=3271 lang=python3
# @lcpr version=30204
#
# [3271] 哈希分割字符串
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def stringHash(self, s: str, k: int) -> str:
        ret=[]
        for i in range(len(s)//k):
            ss=sum(ord(ch)-97 for ch in s[i*k:i*k+k])
            ret.append(chr(ss%26 + 97))
        return ''.join(ret)
# @lc code=end
assert Solution().stringHash(s = "mxz", k = 3)=='i'
assert Solution().stringHash(s = "abcd", k = 2)=='bf'


#
# @lcpr case=start
# "abcd"\n2\n
# @lcpr case=end

# @lcpr case=start
# "mxz"\n3\n
# @lcpr case=end

#

