#
# @lc app=leetcode.cn id=2929 lang=python3
# @lcpr version=30204
#
# [2929] 给小朋友们分糖果 II
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if (n + 2) // 3 > limit:
            return 0
        tot = (n + 2) * (n + 1) // 2
        invalid1 =0 if limit+1>n else (1 + n - limit) * (n - limit) // 2 * 3
        invalid2 =0 if 2*limit+2>n else (n - 2 * limit) * (n - 1 - 2 * limit) // 2 * 3
        return tot - invalid1 + invalid2


# @lc code=end
assert Solution().distributeCandies(6,2) == 1
assert Solution().distributeCandies(1,3) == 3
assert Solution().distributeCandies(3, 3) == 10
assert Solution().distributeCandies(5, 2) == 3


#
# @lcpr case=start
# 5\n2\n
# @lcpr case=end

# @lcpr case=start
# 3\n3\n
# @lcpr case=end

#
