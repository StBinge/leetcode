#
# @lc app=leetcode.cn id=2824 lang=python3
# @lcpr version=30204
#
# [2824] 统计和小于目标的下标对数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left,right=0,len(nums)-1
        ret=0
        while left<right:
            if nums[left]+nums[right]<target:
                ret+=right-left
                left+=1
            else:
                right-=1
        return ret
# @lc code=end
assert Solution().countPairs([-6,2,5,-2,-7,-1,3],-2)==10
assert Solution().countPairs(nums = [-1,1,2,3,1], target = 2)==3


#
# @lcpr case=start
# [-1,1,2,3,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [-6,2,5,-2,-7,-1,3]\n-2\n
# @lcpr case=end

#

