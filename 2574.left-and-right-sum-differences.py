#
# @lc app=leetcode.cn id=2574 lang=python3
# @lcpr version=30204
#
# [2574] 左右元素和的差值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:     
        ret=[]
        left,right=0,sum(nums)
        for n in nums:
            right-=n
            ret.append(abs(right-left))
            left+=n
        return ret
# @lc code=end
assert Solution().leftRightDifference([10,4,8,3])==[15,1,11,22]


#
# @lcpr case=start
# [10,4,8,3]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

