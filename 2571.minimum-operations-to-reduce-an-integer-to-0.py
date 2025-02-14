#
# @lc app=leetcode.cn id=2571 lang=python3
# @lcpr version=30204
#
# [2571] 将整数减少到零需要的最少操作数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, n: int) -> int:
        ret=1
        while n&(n-1):
            lowbit=n&(-n)
            if n&(lowbit<<1):
                n+=lowbit
            else:
                n-=lowbit
            ret+=1
        return ret

# @lc code=end
assert Solution().minOperations(54)==3
assert Solution().minOperations(39)==3


#
# @lcpr case=start
# 39\n
# @lcpr case=end

# @lcpr case=start
# 54\n
# @lcpr case=end

#

