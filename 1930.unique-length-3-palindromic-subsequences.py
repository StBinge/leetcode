#
# @lc app=leetcode.cn id=1930 lang=python3
# @lcpr version=30204
#
# [1930] 长度为 3 的不同回文子序列
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        N=len(s)
        ret = set()
        left_mask=[0]*N
        right_mask=[0]*N
        lmask=rmask=0
        orda=ord('a')
        masks=[0]*26
        for i in range(N):
            left_mask[i]=lmask
            right_mask[-1-i]=rmask
            lmask|=1<<(ord(s[i])-orda)
            rmask|=1<<(ord(s[-1-i])-orda)
        for i in range(1,N-1):
            ml,mr=left_mask[i],right_mask[i]
            code=ord(s[i])-orda
            masks[code]|=(ml&mr)
        return sum(m.bit_count() for m in masks)

# @lc code=end
assert Solution().countPalindromicSubsequence("bbcbaba") == 4
assert Solution().countPalindromicSubsequence("abc") == 0
assert Solution().countPalindromicSubsequence("aabca") == 3


#
# @lcpr case=start
# "aabca"\n
# @lcpr case=end

# @lcpr case=start
# "adc"\n
# @lcpr case=end

# @lcpr case=start
# "bbcbaba"\n
# @lcpr case=end

#
