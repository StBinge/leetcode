#
# @lc app=leetcode.cn id=1781 lang=python3
#
# [1781] 所有子字符串美丽值之和
#
from sbw import *
# @lc code=start
class Solution:
    def beautySum(self, s: str) -> int:
        N=len(s)
        ret=0
        for i in range(N-1):
            for j in range(i+1,N):
                cnt=Counter(s[i:j+1])
                ret+=(max(cnt.values())-min(cnt.values()))
        return ret
# @lc code=end
assert Solution().beautySum('aabcbaa')==17
assert Solution().beautySum('aabcb')==5
