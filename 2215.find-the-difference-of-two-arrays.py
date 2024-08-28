#
# @lc app=leetcode.cn id=2215 lang=python3
# @lcpr version=30204
#
# [2215] 找出两数组的不同
#
from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        cache = defaultdict(int)
        for n in nums1:
            cache[n] |= 1
        for n in nums2:
            cache[n] |= 2
        ret = [[], []]
        for k, v in cache.items():
            if v == 3:
                continue
            ret[v - 1].append(k)
        return ret


# @lc code=end
assert Solution().findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6]) == [[1, 3], [4, 6]]


#
# @lcpr case=start
# [1,2,3]\n[2,4,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,3]\n[1,1,2,2]\n
# @lcpr case=end

#
