#
# @lc app=leetcode.cn id=2541 lang=python3
# @lcpr version=30204
#
# [2541] 使数组中所有元素相等的最小操作数 II
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            return 0 if all(x1 == x2 for x1, x2 in zip(nums1, nums2)) else -1
        if sum(nums1) != sum(nums2):
            return -1
        ret = 0
        for x1, x2 in zip(nums1, nums2):
            dif = x1 - x2
            if dif % k:
                return -1
            if dif > 0:
                ret += dif // k
        return ret


# @lc code=end
assert Solution().minOperations([10, 5, 15, 20], [20, 10, 15, 5], 0) == -1


#
# @lcpr case=start
# [4,3,1,4]\n[1,3,7,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [3,8,5,2]\n[2,4,1,6]\n1\n
# @lcpr case=end

#
