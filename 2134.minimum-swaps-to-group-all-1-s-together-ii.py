#
# @lc app=leetcode.cn id=2134 lang=python3
# @lcpr version=30204
#
# [2134] 最少交换次数来组合所有的 1 II
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        tot=nums.count(1)
        ret=0
        for i in range(tot):
            ret+=1-nums[i]

        N=len(nums)
        cur=ret
        for i in range(1,N):
            cur-=1-nums[i-1]
            cur+=1-nums[(i+tot-1)%N]
            ret=min(ret,cur)
        return ret
# @lc code=end



#
# @lcpr case=start
# [0,1,0,1,1,0,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1,1,0,0,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,0,0,1]\n
# @lcpr case=end

#

