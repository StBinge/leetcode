#
# @lc app=leetcode.cn id=3095 lang=python3
# @lcpr version=30204
#
# [3095] 或值至少 K 的最短子数组 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        cur = dict()
        for i, x in enumerate(nums):
            cur = {_or | x: left for _or, left in cur.items()}
            cur[x] = i
            for _or, left in cur.items():
                if _or >= k:
                    ans = min(ans, i - left + 1)
        return ans if ans != float('inf') else -1

                


# @lc code=end
assert Solution().minimumSubarrayLength([1],0)==1
assert Solution().minimumSubarrayLength([1,2,3],2)==1
assert Solution().minimumSubarrayLength([2,1,8],10)==3


#
# @lcpr case=start
# [1,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,1,8]\n10\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

#

