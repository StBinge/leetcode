#
# @lc app=leetcode.cn id=1652 lang=python3
#
# [1652] 拆炸弹
#
from sbw import *


# @lc code=start
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        ret = [0] * N
        if k == 0:
            return ret
        if k<0:
            l,r=N+k,N
        if k>0:
            l,r=1,k+1
        window=sum(code[l:r])
        for i in range(N):
            ret[i]=window
            window-=code[l%N]
            window+=code[r%N]
            l=(l+1)
            r=(r+1)
        return ret



# @lc code=end
assert Solution().decrypt([2,4,9,3],-2) == [12,5,6,13]
assert Solution().decrypt([5, 7, 1, 4], 3) == [12, 10, 16, 13]
