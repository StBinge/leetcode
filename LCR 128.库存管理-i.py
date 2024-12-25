#
# @lc app=leetcode.cn id=LCR 128 lang=python3
# @lcpr version=30204
#
# [LCR 128] 库存管理 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def inventoryManagement(self, stock: List[int]) -> int:
        ret=stock[0]
        for i in range(len(stock)-1,0,-1):
            if stock[i]<stock[i-1]:
                ret=min(ret,stock[i])
                break
        return ret
# @lc code=end



#
# @lcpr case=start
# [4,5,8,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [5,7,9,1,2]\n
# @lcpr case=end

#

