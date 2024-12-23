#
# @lc app=leetcode.cn id=2582 lang=python3
# @lcpr version=30204
#
# [2582] 递枕头
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        k,m=divmod(time,n-1)
        if k&1:
            return n-m
        return 1+m
        
# @lc code=end
assert Solution().passThePillow(3,2)==3
assert Solution().passThePillow(4,5)==2


#
# @lcpr case=start
# 4\n5\n
# @lcpr case=end

# @lcpr case=start
# 3\n2\n
# @lcpr case=end

#

