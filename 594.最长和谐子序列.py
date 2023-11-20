#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#
from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter=Counter(nums)
        ret=0
        for k in counter:
            if k+1 in counter:
                ret=max(ret,counter[k]+counter[k+1])
        return ret
# @lc code=end
assert Solution().findLHS([1,3,2,2,5,2,3,7])==5
assert Solution().findLHS([1,2,3,4])==2
assert Solution().findLHS([1,1,1,1])==0
