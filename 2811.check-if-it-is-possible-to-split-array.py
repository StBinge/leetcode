#
# @lc app=leetcode.cn id=2811 lang=python3
# @lcpr version=30204
#
# [2811] 判断是否能拆分数组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        return len(nums)<3 or any(x+y>=m for x,y in pairwise(nums))
    
# @lc code=end
assert Solution().canSplitArray([1,1],3)
assert Solution().canSplitArray([1],1)
assert Solution().canSplitArray([2,2,1],4)
assert Solution().canSplitArray([2,2,1],4)


#
# @lcpr case=start
# [2, 2, 1]\n4\n
# @lcpr case=end

# @lcpr case=start
# [2, 1, 3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [2, 3, 3, 2, 3]\n6\n
# @lcpr case=end

#

