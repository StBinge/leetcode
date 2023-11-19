#
# @lc app=leetcode.cn id=372 lang=python3
#
# [372] 超级次方
#
from typing import List
# @lc code=start

class Solution:

    def superPow(self, a: int, b: List[int]) -> int:
        ans=1
        mod=1337

        for e in reversed(b):
            ans=ans*pow(a,e,mod) % mod
            # ans%=mod
            a=pow(a,10,mod)
        return int(ans)
# @lc code=end

