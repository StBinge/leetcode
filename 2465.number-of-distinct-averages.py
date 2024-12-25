#
# @lc app=leetcode.cn id=2465 lang=python3
# @lcpr version=30204
#
# [2465] 不同的平均值数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        seen=set()
        left,right=0,len(nums)-1
        while left<=right:
            seen.add(nums[left]+nums[right])
            left+=1
            right-=1
        return len(seen)
# @lc code=end



#
# @lcpr case=start
# [4,1,4,0,3,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,100]\n
# @lcpr case=end

#

