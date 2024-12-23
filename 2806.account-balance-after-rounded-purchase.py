#
# @lc app=leetcode.cn id=2806 lang=python3
# @lcpr version=30204
#
# [2806] 取整购买后的账户余额
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100-(purchaseAmount+5)//10*10
        
# @lc code=end
assert Solution().accountBalanceAfterPurchase(9)==90


#
# @lcpr case=start
# 9\n
# @lcpr case=end

# @lcpr case=start
# 15\n
# @lcpr case=end

#

