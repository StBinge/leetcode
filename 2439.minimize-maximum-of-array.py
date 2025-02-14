#
# @lc app=leetcode.cn id=2439 lang=python3
# @lcpr version=30204
#
# [2439] 最小化数组中的最大值
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        s=0
        avg=0
        for i,n in enumerate(nums):
            s+=n
            if n>avg:
                avg=max(avg,(s-1)//(i+1)+1)
        return avg


# @lc code=end
assert Solution().minimizeArrayValue([13,13,20,0,8,9,9])==16
assert Solution().minimizeArrayValue([10,1])==10
assert Solution().minimizeArrayValue([3,7,1,6])==5


#
# @lcpr case=start
# [3,7,1,6]\n
# @lcpr case=end

# @lcpr case=start
# [10,1]\n
# @lcpr case=end

#

