#
# @lc app=leetcode.cn id=3020 lang=python3
#
# [3020] 子集中元素的最大数量
#
from sbw import *
# @lc code=start
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        s=Counter(nums)
        # nums.sort()
        ones=s[1]
        ret=ones-1 | 1
        del s[1]


        for n in nums:
            l=0
            while s[n]>1:
                l+=2
                n*=n
            l+=s[n]
            ret=max(ret,l-1 | 1) 
        return ret
# @lc code=end
assert Solution().maximumLength([4,36,9,16,1,1,4,121,64,4])==3
assert Solution().maximumLength([14,14,196,196,38416,38416])==5
assert Solution().maximumLength([1,16,49,16,121])==1
assert Solution().maximumLength([5,4,1,2,2])==3
assert Solution().maximumLength([1,3,2,4])==1
