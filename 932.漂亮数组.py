#
# @lc app=leetcode.cn id=932 lang=python3
#
# [932] 漂亮数组
#
from sbw import *
# @lc code=start
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        f=[[] for _ in range(n+1)]
        f[1]=[1]
        for i in range(2,n+1):
            odds=(i+1)//2
            evens=i//2
            f[i]=[x*2-1 for x in f[odds]]+[x*2 for x in f[evens]]
        return f[-1]
# @lc code=end
print(Solution().beautifulArray(5))
print(Solution().beautifulArray(4))
