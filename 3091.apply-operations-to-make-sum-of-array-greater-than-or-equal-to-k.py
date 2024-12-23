#
# @lc app=leetcode.cn id=3091 lang=python3
# @lcpr version=30204
#
# [3091] 执行操作使数据元素之和大于等于 K
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, k: int) -> int:
        rt=max(1,math.isqrt(k-1))
        return min(rt-1 + (k-1)//rt, rt + (k-1)//(rt+1))


# @lc code=end
assert Solution().minOperations(36)==10
assert Solution().minOperations(1)==0
assert Solution().minOperations(11)==5


#
# @lcpr case=start
# 11\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

