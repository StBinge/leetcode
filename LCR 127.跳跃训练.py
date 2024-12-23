#
# @lc app=leetcode.cn id=LCR 127 lang=python3
# @lcpr version=30204
#
# [LCR 127] 跳跃训练
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def trainWays(self, num: int) -> int:
        if num<=2:
            return max(1,num)
        f1=1
        f2=2
        for i in range(3,num+1):
            f1,f2=f2,(f1+f2)%(10**9+7)
        return f2
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 5\n
# @lcpr case=end

#

