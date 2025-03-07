#
# @lc app=leetcode.cn id=3234 lang=python3
# @lcpr version=30204
#
# [3234] 统计 1 显著的字符串的数量
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt1=ret=0
        N=len(s)
        for i,ch in enumerate(s):
            cnt1+=ord(ch)&1
            L=i+1
            ret+= cnt1>=(L-cnt1)**2
            _cnt1=cnt1
            for j in range(i+1,N):
                _cnt1+=(ord(s[j])&1)-(ord(s[j-L])&1)
                ret+= _cnt1>=(L-_cnt1)**2
        return ret

# @lc code=end
assert Solution().numberOfSubstrings('101101')==16
assert Solution().numberOfSubstrings('00011')==5


#
# @lcpr case=start
# "00011"\n
# @lcpr case=end

# @lcpr case=start
# "101101"\n
# @lcpr case=end

#

