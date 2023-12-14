#
# @lc app=leetcode.cn id=940 lang=python3
#
# [940] 不同的子序列 II
#

# @lc code=start
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        g=[0]*26
        Mod=10**9+7
        total=0
        for c in s:
            idx=ord(c)-ord('a')
            total,g[idx]=(2*total+1-g[idx])%Mod,(total+1)%Mod

        return total
# @lc code=end
assert Solution().distinctSubseqII('abc')==7
assert Solution().distinctSubseqII('aba')==6
assert Solution().distinctSubseqII('aaa')==3
