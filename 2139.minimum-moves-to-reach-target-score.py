#
# @lc app=leetcode.cn id=2139 lang=python3
# @lcpr version=30204
#
# [2139] 得到目标值的最少行动次数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ret = 0
        while target > 1 and maxDoubles:
            if target & 1:
                target -= 1
                ret += 1
            target >>= 1
            ret += 1
            maxDoubles -= 1
        return ret + target - 1


# @lc code=end
assert Solution().minMoves(10, 4) == 4
assert Solution().minMoves(19, 2) == 7
assert Solution().minMoves(5, 0) == 4


#
# @lcpr case=start
# 5\n0\n
# @lcpr case=end

# @lcpr case=start
# 19\n2\n
# @lcpr case=end

# @lcpr case=start
# 10\n4\n
# @lcpr case=end

#
