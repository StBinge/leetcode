#
# @lc app=leetcode.cn id=3043 lang=python3
#
# [3043] 最长公共前缀的长度
#
from sbw import *
# @lc code=start

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        s=set()
        for n in arr1:
            while n:
                s.add(n)
                n//=10
        mx=0
        for n in arr2:
            if mx>=n:
                continue
            while n:
                if n in s:
                    mx=max(mx,n)
                n//=10
        return len(str(mx)) if mx else 0
# @lc code=end
assert Solution().longestCommonPrefix(arr1 = [1,2,3], arr2 = [4,4,4])==0
assert Solution().longestCommonPrefix(arr1 = [1,10,100], arr2 = [1000])==3
