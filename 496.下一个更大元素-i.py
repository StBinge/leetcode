#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#
from typing import List
# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # rights=[-1]*len(nums2)
        stack=[]
        maps={}
        for i in reversed(nums2):
            while stack and i>=stack[-1]:
                stack.pop()
            if stack:
                maps[i]=stack[-1]
            else:
                maps[i]=-1
            stack.append(i)

        return [maps[n] for n in nums1]
# @lc code=end
nums1 = [4,1,2]
nums2 = [1,3,4,2]
assert Solution().nextGreaterElement(nums1,nums2)==[-1,3,-1]
nums1 = [2,4]
nums2 = [1,2,3,4]
assert Solution().nextGreaterElement(nums1,nums2)==[3,-1]
