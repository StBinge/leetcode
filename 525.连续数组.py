#
# @lc app=leetcode.cn id=525 lang=python3
#
# [525] 连续数组
#
from typing import List
# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pre=0
        map={0:-1}
        ret=0
        for i,n in enumerate(nums):
            pre=(1 if n==1 else -1)+pre
            if pre in map:
                ret=max(ret,i-map[pre])
            else:
                map[pre]=i
        return ret
        
# @lc code=end
assert Solution().findMaxLength([0,0,1,0,0,0,1,1])==6
assert Solution().findMaxLength([0,1,1,0,1,1,1,0])==4
assert Solution().findMaxLength([0,1])==2
assert Solution().findMaxLength([0,1,0])==2
