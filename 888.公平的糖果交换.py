#
# @lc app=leetcode.cn id=888 lang=python3
#
# [888] 公平的糖果交换
#
from typing import List
# @lc code=start
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        s1=sum(aliceSizes)
        s2=sum(bobSizes)
        target=(s1-s2)//2
        set_b=set(bobSizes)
        for  a in aliceSizes:
            if a-target in set_b:
                return [a,a-target]

# @lc code=end
aliceSizes = [1,1]
bobSizes = [2,2]
ret= [1,2]
assert Solution().fairCandySwap(aliceSizes,bobSizes)==ret
