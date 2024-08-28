#
# @lc app=leetcode.cn id=1394 lang=python3
#
# [1394] 找出数组中的幸运数
#
from sbw import *
# @lc code=start
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt=Counter(arr)
        ret=-1
        for n,c in cnt.items():
            if n==c and n>ret:
                ret=n
        return ret
# @lc code=end
assert Solution().findLucky([2,2,3,4])==2
