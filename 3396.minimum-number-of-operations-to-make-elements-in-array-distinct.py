#
# @lc app=leetcode.cn id=3396 lang=python3
# @lcpr version=30204
#
# [3396] 使数组元素互不相同所需的最少操作次数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen=set()
        for i in range(len(nums)-1,-1,-1):
            if nums[i] in seen:
                return i//3+1
            seen.add(nums[i])
        return 0

# @lc code=end
assert Solution().minimumOperations([4,5,6,4,4])==2
assert Solution().minimumOperations([1,2,3,4,2,3,3,5,7])==2


#
# @lcpr case=start
# [1,2,3,4,2,3,3,5,7]\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,4,4]\n
# @lcpr case=end

# @lcpr case=start
# [6,7,8,9]\n
# @lcpr case=end

#

