#
# @lc app=leetcode.cn id=3117 lang=python3
# @lcpr version=30204
#
# [3117] 划分数组得到最小的值之和
#
from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        # presums=list(accumulate(nums,initial=0))
        N = len(nums)
        M = len(andValues)
        Mask = (1 << 17) - 1

        @cache
        def dfs(idx1, idx2, val, pre_idx1):
            if idx1 == N and idx2 == M:
                return 0
            if idx1 == N or idx2 == M:
                return float("inf")
            
            ret = float("inf")
            val &= nums[idx1]
            if val == andValues[idx2]:
                ret = nums[idx1] + dfs(idx1 + 1, idx2 + 1, Mask, idx1 + 1)
            ret = min(ret, dfs(idx1 + 1, idx2, val, pre_idx1))
            return ret

        ret = dfs(0, 0, Mask, 0)
        return ret if ret < float("inf") else -1


# @lc code=end
assert Solution().minimumValueSum([16510,16639,16893,16511,16892,17406,16510,17402,16637,17405,16893,17403,17406,17407,16637,17396,16638,17403,16892,16639],[16508,16624,16639]) == 50041
assert Solution().minimumValueSum(nums=[1, 4, 3, 3, 2], andValues=[0, 3, 3, 2]) == 12


#
# @lcpr case=start
# [1,4,3,3,2]\n[0,3,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,5,7,7,7,5]\n[0,7,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n[2]\n
# @lcpr case=end

#
