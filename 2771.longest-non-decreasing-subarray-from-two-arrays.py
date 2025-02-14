#
# @lc app=leetcode.cn id=2771 lang=python3
# @lcpr version=30204
#
# [2771] 构造最长非递减子数组
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:

        f0 = f1 = 1
        ret = 1
        for [x0, y0], [x1, y1] in pairwise(zip(nums1, nums2)):
            _f0 = _f1 = 1
            if x0 <= x1:
                _f0 = f0 + 1
            if y0 <= x1:
                _f0 = max(_f0, f1 + 1)

            if x0 <= y1:
                _f1 = f0 + 1
            if y0 <= y1:
                _f1 = max(_f1, f1 + 1)
            f0, f1 = _f0, _f1
            ret = max(ret, f0, f1)
        return ret


# @lc code=end
assert Solution().maxNonDecreasingLength([8, 7, 4], [13, 4, 4]) == 2
assert Solution().maxNonDecreasingLength([5, 18, 5], [17, 5, 8]) == 3
assert Solution().maxNonDecreasingLength([3, 19, 13, 19], [20, 18, 7, 14]) == 2
assert Solution().maxNonDecreasingLength(nums1=[1, 1], nums2=[2, 2]) == 2
assert Solution().maxNonDecreasingLength(nums1=[1, 3, 2, 1], nums2=[2, 2, 3, 4]) == 4
assert Solution().maxNonDecreasingLength(nums1=[2, 3, 1], nums2=[1, 2, 1]) == 2


#
# @lcpr case=start
# [2,3,1]\n[1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,2,1]\n[2,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n[2,2]\n
# @lcpr case=end

#
