#
# @lc app=leetcode.cn id=2370 lang=python3
# @lcpr version=30204
#
# [2370] 最长理想子序列
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        f0=[0]*26
        # f1=[0]*26
        code=lambda x:ord(x)-97
        for ch in s:
            c=code(ch)
            f1=max(f0[max(c-k,0):min(26,c+k+1)],default=0)+1
            f0[c]=f1
        return max(f0)
# @lc code=end
assert Solution().longestIdealString("azaza",25)==5
assert Solution().longestIdealString(s = "abcd", k = 3)==4
assert Solution().longestIdealString(s = "acfgbd", k = 2)==4


#
# @lcpr case=start
# "acfgbd"\n2\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n3\n
# @lcpr case=end

#

