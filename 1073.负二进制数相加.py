#
# @lc app=leetcode.cn id=1073 lang=python3
#
# [1073] 负二进制数相加
#
from sbw import *


# @lc code=start
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        L1, L2 = len(arr1), len(arr2)
        if L1 < L2:
            arr1, arr2 = arr2, arr1
            L1, L2 = L2, L1
        # i1=L1-1
        i2 = L2 - 1
        ret = []
        carry = 0
        for i in range(L1-1,-1,-1):
            if i2 < 0:
                bit2 = 0
            else:
                bit2 = arr2[i2]
                i2 -= 1
            val = carry + arr1[i] + bit2
            bit = val % 2
            carry = (val - bit) // -2
            ret.append(bit)

        if carry == 1:
            ret.append(1)
        elif carry == -1:
            ret.extend([1, 1])
        while len(ret)>1 and ret[-1]==0:
            ret.pop()
        return ret[::-1]


# @lc code=end
assert Solution().addNegabinary(arr1=[1], arr2=[1,1]) == [0]
assert Solution().addNegabinary(arr1=[0], arr2=[1,0]) == [1,0]
assert Solution().addNegabinary(arr1=[0], arr2=[0]) == [0]
assert Solution().addNegabinary(arr1=[1, 1, 1, 1, 1], arr2=[1, 0, 1]) == [1, 0, 0, 0, 0]
