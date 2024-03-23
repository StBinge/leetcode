#
# @lc app=leetcode.cn id=1475 lang=python3
#
# [1475] 商品折扣后的最终价格
#
from sbw import *
# @lc code=start
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        L=len(prices)
        stack=[prices[-1]]
        mins=[0]*L
        for i in range(L-2,-1,-1):
            n=prices[i]
            while stack and n<stack[-1]:
                stack.pop()
            if stack:
                mins[i]=stack[-1]
            stack.append(n)
        ret=[0]*L
        for i in range(L):
            ret[i]=prices[i]-mins[i]
        return ret

# @lc code=end
assert Solution().finalPrices([10,1,1,6])==[9,0,1,6]
assert Solution().finalPrices([8,4,6,2,3])==[4,2,4,2,3]
