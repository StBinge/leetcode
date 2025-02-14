#
# @lc app=leetcode.cn id=3364 lang=python3
# @lcpr version=30204
#
# [3364] 最小正和子数组
#
from sbw import *
from sortedcontainers import SortedList

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        presums = list(accumulate(nums, initial=0))
        sl = SortedList()
        ret = float("inf")
        for i in range(l, len(nums) + 1):
            sl.add(presums[i - l])
            k = sl.bisect_left(presums[i])
            if k:
                ret = min(ret, presums[i] - sl[k-1])
            if i >= r:
                sl.remove(presums[i - r])
        return ret if ret !=float('inf') else -1


# @lc code=end
assert Solution().minimumSumSubarray([-12,8],1,1) == 8
assert Solution().minimumSumSubarray([-2, 2, -3, 1], 2, 3) == -1
assert Solution().minimumSumSubarray([3, -2, 1, 4], 2, 3) == 1


#
# @lcpr case=start
# [3, -2, 1, 4]\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# [-2, 2, -3, 1]\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# [1, 2, 3, 4]\n2\n4\n
# @lcpr case=end

#
