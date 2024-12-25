#
# @lc app=leetcode.cn id=2834 lang=python3
# @lcpr version=30204
#
# [2834] 找出美丽数组的最小和
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        mod = 10**9 + 7
        head = target // 2
        if n <= head:
            return (1 + n) * n // 2 % mod
        ret = (1 + head) * head // 2 % mod
        end_cnt = n - head
        return (ret + (target + target + end_cnt - 1) * end_cnt // 2) % mod


# @lc code=end


#
# @lcpr case=start
# 2\n3\n
# @lcpr case=end

# @lcpr case=start
# 3\n3\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n
# @lcpr case=end

#
