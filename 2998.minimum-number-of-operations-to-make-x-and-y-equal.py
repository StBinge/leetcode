#
# @lc app=leetcode.cn id=2998 lang=python3
# @lcpr version=30204
#
# [2998] 使 X 和 Y 相等的最少操作次数
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        @cache
        def dfs(v):
            if v<=y:
                return y-v
            return min(v-y,
                    dfs(v//11)+v%11+1,
                    dfs(v//11+1)+1+11-v%11,
                    dfs(v//5)+v%5+1,
                    dfs(v//5+1)+1+5-v%5,
                    )

        return dfs(x)

# @lc code=end
assert Solution().minimumOperationsToMakeEqual(25, 30) == 5
assert Solution().minimumOperationsToMakeEqual(54, 2) == 4
assert Solution().minimumOperationsToMakeEqual(26, 1) == 3


#
# @lcpr case=start
# 26\n1\n
# @lcpr case=end

# @lcpr case=start
# 54\n2\n
# @lcpr case=end

# @lcpr case=start
# 25\n30\n
# @lcpr case=end

#
