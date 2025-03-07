#
# @lc app=leetcode.cn id=3350 lang=python3
# @lcpr version=30204
#
# [3350] 检测相邻递增子数组 II
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        cnt=0
        pre=float('-inf')
        pre_cnt=0
        ret=0
        for i,n in enumerate(nums):
            if n>pre:
                cnt+=1
            else:
                ret=max(ret,min(cnt,pre_cnt),cnt//2)
                pre_cnt=cnt
                cnt=1
            pre=n
        return max(ret,min(cnt,pre_cnt),cnt//2)
# @lc code=end
assert Solution().maxIncreasingSubarrays( [1,2,3,4,4,4,4,5,6,7])==2
assert Solution().maxIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1])==3


#
# @lcpr case=start
# [2,5,7,8,9,2,3,4,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,4,4,4,5,6,7]\n
# @lcpr case=end

#

