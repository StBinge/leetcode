#
# @lc app=leetcode.cn id=3083 lang=python3
#
# [3083] 字符串及其反转中是否存在同一子字符串
#
from sbw import *
# @lc code=start

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        L=len(s)
        mask=[0]*26
        orda=ord('a')
        for x,y in pairwise(map(ord,s)):
            x,y=x-orda,y-orda
            mask[x]|=1<<y
            if mask[y] >> x &1:
                return True
        return False
# @lc code=end
assert Solution().isSubstringPresent('uuxqvxrlh')
assert Solution().isSubstringPresent('leafbcaef')
