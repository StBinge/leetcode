#
# @lc app=leetcode.cn id=3178 lang=python3
# @lcpr version=30204
#
# [3178] 找出 K 秒后拿着球的孩子
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        roud,m=divmod(k,n-1)
        if roud&1:
            return n-1-m
        return m
# @lc code=end

assert Solution().numberOfChild(5,6)==2
assert Solution().numberOfChild(3,5)==1

#
# @lcpr case=start
# 3\n5\n
# @lcpr case=end

# @lcpr case=start
# 5\n6\n
# @lcpr case=end

# @lcpr case=start
# 4\n2\n
# @lcpr case=end

#

