#
# @lc app=leetcode.cn id=2216 lang=python3
# @lcpr version=30204
#
# [2216] 美化数组的最少删除数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        ret=0
        N=len(nums)
        for i in range(N):
            idx=i-ret
            if idx%2:
                continue
            if i+1<N and nums[i]==nums[i+1]:
                ret+=1
        return ret+ ((N-ret)&1)

# @lc code=end
assert Solution().minDeletion([1,1,2,2,3,3])==2
assert Solution().minDeletion([1,1,2,3,5])==1


#
# @lcpr case=start
# [1,1,2,3,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,2,3,3]\n
# @lcpr case=end

#

