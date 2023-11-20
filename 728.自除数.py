#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#
from typing import List
# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ret=[]
        for n in range(left,right+1):
            N=n
            while n>0:
                d=n%10
                if d==0 or N%d:
                    break
                n//=10
            else:
                ret.append(N)
        return ret
# @lc code=end

