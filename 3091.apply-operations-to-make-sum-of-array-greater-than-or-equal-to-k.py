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
        x=math.isqrt(k)
        cnt1=x-1 + (k-1)//x
        cnt2=x + (k-1)//(x+1)
        return min(cnt1,cnt2)
# @lc code=end



#
# @lcpr case=start
# 11\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

