#
# @lc app=leetcode.cn id=2616 lang=python3
# @lcpr version=30204
#
# [2616] 最小化数对的最大差值
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        N = len(nums)
        nums.sort()

        def check(x):
            idx = 0
            cnt = 0
            while idx + 1 < N:
                if nums[idx + 1] - nums[idx] <= x:
                    cnt += 1
                    idx += 2
                else:
                    idx += 1
            return cnt >= p
        mx = nums[-1] - nums[0]
        return bisect_left(range(mx),True,key=check)


# @lc code=end
assert Solution().minimizeMax([3, 4, 2, 3, 2, 1, 2], 3) == 1
assert Solution().minimizeMax(nums=[4, 2, 1, 2], p=1) == 0
assert Solution().minimizeMax(nums=[10, 1, 2, 7, 1, 3], p=2) == 1


#
# @lcpr case=start
# [10,1,2,7,1,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [4,2,1,2]\n1\n
# @lcpr case=end

#
