#
# @lc app=leetcode.cn id=2293 lang=python3
# @lcpr version=30204
#
# [2293] 极大极小游戏
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        N=len(nums)
        while N>1:
            N>>=1
            for i in range(0,N):
                if i&1==0:
                    nums[i]=min(nums[2*i],nums[2*i+1])
                else:
                    nums[i]=max(nums[i*2],nums[i*2+1])
        return nums[0]
# @lc code=end
assert Solution().minMaxGame([1,3,5,2,4,8,2,2])==1


#
# @lcpr case=start
# [1,3,5,2,4,8,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3]\n
# @lcpr case=end

#

