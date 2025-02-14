#
# @lc app=leetcode.cn id=2401 lang=python3
# @lcpr version=30204
#
# [2401] 最长优雅子数组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        ret=1
        left=0
        mask=0
        for right,n in enumerate(nums):
            while mask & n:
                mask ^=nums[left]
                left+=1
            ret=max(ret,right-left+1)
            mask|=n
        return max(ret,len(nums)-left)
# @lc code=end
assert Solution().longestNiceSubarray([135745088,609245787,16,2048,2097152])==3
assert Solution().longestNiceSubarray([3,1,5,11,13])==1
assert Solution().longestNiceSubarray([1,3,8,48,10])==3


#
# @lcpr case=start
# [1,3,8,48,10]\n
# @lcpr case=end

# @lcpr case=start
# [3,1,5,11,13]\n
# @lcpr case=end

#

