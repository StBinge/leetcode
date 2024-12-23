#
# @lc app=leetcode.cn id=面试题 08.01 lang=python3
# @lcpr version=30204
#
# [面试题 08.01] 三步问题
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def waysToStep(self, n: int) -> int:
        f=[1,1,2,4]
        for i in range(4,n+1):
            f.append((f[i-1]+f[i-2]+f[i-3])%(10**9+7))
        return f[n]
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 5\n
# @lcpr case=end

#

