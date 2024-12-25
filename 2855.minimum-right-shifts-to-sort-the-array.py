#
# @lc app=leetcode.cn id=2855 lang=python3
# @lcpr version=30204
#
# [2855] 使数组成为递增数组的最少右移次数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        cnt=0
        idx=-1
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                if cnt==1:
                    return -1
                cnt+=1
                idx=i
        if cnt==0:
            return 0
        if nums[0]<nums[-1]:
            return -1
        return len(nums)-idx
# @lc code=end



#
# @lcpr case=start
# [3,4,5,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,4]\n
# @lcpr case=end

#

