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
        if 
   

        difs = [[abs(nums[i] - nums[i + 1]), i, i + 1] for i in range(N - 1)]
        used = [False] * N
        difs.sort()
        for [dif, i, j] in difs:
            if used[i] or used[j]:
                continue
            p -= 1
            if p == 0:
                return dif
            used[i] = used[j] = True


# @lc code=end
assert Solution().minimizeMax([3,4,2,3,2,1,2],3) == 0
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
