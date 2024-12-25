#
# @lc app=leetcode.cn id=2591 lang=python3
# @lcpr version=30204
#
# [2591] 将钱分给最多的儿童
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if children > money:
            return -1
        if children + 7 > money:
            return 0
        if children * 8 <= money:
            return children - (children*8<money)
        extra = money - children
        d, m = divmod(extra, 7)
        if children - d == 1 and m == 3:
            return d - 1
        else:
            return d


# @lc code=end
assert Solution().distMoney(24,2) == 1
assert Solution().distMoney(16, 2) == 2
assert Solution().distMoney(20, 3) == 1


#
# @lcpr case=start
# 20\n3\n
# @lcpr case=end

# @lcpr case=start
# 16\n2\n
# @lcpr case=end

#
