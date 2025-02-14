#
# @lc app=leetcode.cn id=2826 lang=python3
# @lcpr version=30204
#
# [2826] 将三个组排序
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        f=[0]*4
        for n in nums:
            for j in range(3,0,-1):
                f[j]=min(f[k] for k in range(1,j+1))+(j!=n)
        return min(f[1:])


# @lc code=end
assert Solution().minimumOperations([2, 1, 3, 2, 1]) == 3
assert Solution().minimumOperations([1]) == 0
assert Solution().minimumOperations([2, 2, 2, 2, 3, 3]) == 0
assert Solution().minimumOperations([1, 3, 2, 1, 3, 3]) == 2


#
# @lcpr case=start
# [2,1,3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,2,1,3,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,3,3]\n
# @lcpr case=end

#
