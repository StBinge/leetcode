#
# @lc app=leetcode.cn id=1438 lang=python3
#
# [1438] 绝对差不超过限制的最长连续子数组
#
from sbw import *
# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_stack=deque()
        max_stack=deque()
        left=0
        ret=0
        for right,n in enumerate(nums):
            while min_stack and n<=nums[min_stack[-1]]:
                min_stack.pop()
            min_stack.append(right)
            while max_stack and n>=nums[max_stack[-1]]:
                max_stack.pop()
            max_stack.append(right)
            if nums[max_stack[0]]-nums[min_stack[0]]<=limit:
                ret=max(ret,right-left+1)
            else:
                while True:
                    left=min(max_stack[0],min_stack[0])+1
                    if min_stack[0]<left:
                        min_stack.popleft()
                    if max_stack[0]<left:
                        max_stack.popleft()
                    if nums[max_stack[0]]-nums[min_stack[0]]<=limit:
                        break
        return ret
# @lc code=end
assert Solution().longestSubarray(nums = [4,2,2,2,4,4,2,2], limit = 0)==3
assert Solution().longestSubarray(nums = [10,1,2,4,7,2], limit = 5)==4
assert Solution().longestSubarray(nums = [8,2,4,7], limit = 4)==2
