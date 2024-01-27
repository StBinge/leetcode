#
# @lc app=leetcode.cn id=1144 lang=python3
#
# [1144] 递减元素使数组呈锯齿状
#
from sbw import *
# @lc code=start
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        L=len(nums)

        def count(offset):
            ret=0
            # arr=nums.copy()
            for i in range(offset,L,2):
                edge=1001
                if i-1>=0:
                    edge=min(edge,nums[i-1])
                if i+1<L:
                    edge=min(edge,nums[i+1])
                ret+=max(0,(nums[i]-edge)+1)
            return ret
        return min(count(0),count(1))
# @lc code=end
assert Solution().movesToMakeZigzag([2,7,10,9,8,9])==4
assert Solution().movesToMakeZigzag([9,6,1,6,2])==4
assert Solution().movesToMakeZigzag([1,2,3])==2
