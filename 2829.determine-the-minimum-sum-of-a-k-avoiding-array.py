#
# @lc app=leetcode.cn id=2829 lang=python3
# @lcpr version=30204
#
# [2829] k-avoiding 数组的最小总和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        less=k//2
        if n<=less:
            return (1+n)*n//2
        more=n-less
        return (1+less)*less//2 + (k+k+more-1)*more//2
    
# @lc code=end
assert Solution().minimumSum(2,6)==3
assert Solution().minimumSum(5,4)==18


#
# @lcpr case=start
# 5\n4\n
# @lcpr case=end

# @lcpr case=start
# 2\n6\n
# @lcpr case=end

#

