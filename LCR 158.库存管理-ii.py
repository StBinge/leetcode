#
# @lc app=leetcode.cn id=LCR 158 lang=python3
# @lcpr version=30204
#
# [LCR 158] 库存管理 II
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def inventoryManagement(self, stock: List[int]) -> int:
        cnt=0
        pre=-1
        for s in stock:
            if s==pre:
                cnt+=1
            elif cnt==0:
                pre=s
                cnt=1
            else:
                cnt-=1
        return pre
                

# @lc code=end



#
# @lcpr case=start
# [6, 1, 3, 1, 1, 1]\n
# @lcpr case=end

#

