#
# @lc app=leetcode.cn id=1546 lang=python3
#
# [1546] 和为目标值且不重叠的非空子数组的最大数目
#
from sbw import *
# @lc code=start
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        vis={0}
        tot=0
        ret=0
        for n in nums:
            tot+=n
            pair=tot-target
            if pair in vis:
                ret+=1
                vis={0}
                tot=0
            else:
                vis.add(tot)
        return ret
# @lc code=end
assert Solution().maxNonOverlapping(nums = [0,0,0], target = 0)==3
assert Solution().maxNonOverlapping(nums = [-2,6,6,3,5,4,1,2,8], target = 10)==3
assert Solution().maxNonOverlapping(nums = [-1,3,5,1,4,2,-9], target = 6)==2
assert Solution().maxNonOverlapping(nums = [1,1,1,1,1], target = 2)==2
