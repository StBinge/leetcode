#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#
from typing import List
# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        ret=[0]*(n+1)

        for i in range(1,n+1):
            ret[i]=ret[i&(i-1)]+1
        return ret
# @lc code=end

print(Solution().countBits(2))
print(Solution().countBits(5))
