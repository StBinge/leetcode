#
# @lc app=leetcode.cn id=2593 lang=python3
# @lcpr version=30204
#
# [2593] 标记所有元素后数组的分数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findScore(self, nums: List[int]) -> int:
        N=len(nums)
        idx=0
        score=0
        while idx<N:
            i0=idx
            while idx+1<N and nums[idx+1]<nums[idx]:
                idx+=1
            for j in range(idx,i0-1,-2):
                score+=nums[j]
            idx+=2
        return score
# @lc code=end
assert Solution().findScore([6,5,4,8,7,5,3,2])==17


#
# @lcpr case=start
# [2,1,3,4,5,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,5,1,3,2]\n
# @lcpr case=end

#

