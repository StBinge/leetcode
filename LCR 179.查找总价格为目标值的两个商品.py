#
# @lc app=leetcode.cn id=LCR 179 lang=python3
# @lcpr version=30204
#
# [LCR 179] 查找总价格为目标值的两个商品
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def twoSum(self, price: List[int], target: int) -> List[int]:
        l,r=0,len(price)-1
        while True:
            s= price[l]+price[r]
            if s==target:
                return [price[l],price[r]]
            elif s<target:
                l+=1
            else:
                r-=1
# @lc code=end



#
# @lcpr case=start
# [3, 9, 12, 15]\n18\n
# @lcpr case=end

# @lcpr case=start
# [8, 21, 27, 34, 52, 66]\n61\n
# @lcpr case=end

#

