#
# @lc app=leetcode.cn id=2576 lang=python3
# @lcpr version=30204
#
# [2576] 求出最多标记下标
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        left=0
        for x in nums[(N+1)//2:]:
            if nums[left]*2<=x:
                left+=1
        return left*2

# @lc code=end
assert Solution().maxNumOfMarkedIndices([42,83,48,10,24,55,9,100,10,17,17,99,51,32,16,98,99,31,28,68,71,14,64,29,15,40]) == 26
assert Solution().maxNumOfMarkedIndices([7, 6, 8]) == 0
assert Solution().maxNumOfMarkedIndices([9, 2, 5, 4]) == 4
assert Solution().maxNumOfMarkedIndices([3, 5, 2, 4]) == 2


#
# @lcpr case=start
# [3,5,2,4]\n
# @lcpr case=end

# @lcpr case=start
# [9,2,5,4]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,8]\n
# @lcpr case=end

#
