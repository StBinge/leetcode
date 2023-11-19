#
# @lc app=leetcode.cn id=483 lang=python3
#
# [483] 最小好进制
#

# @lc code=start
import math
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        N=int(n)
        maxM=int(math.log2(N))
        for m in range(maxM,0,-1):
            k=int(math.pow(N,1/m))
            if k<=1:
                continue
            base=1
            s=0
            for i in range(m+1):
                s+=base
                base*=k
            if s==N:
                return str(k)
        return str(N-1)

                
# @lc code=end

assert Solution().smallestGoodBase('13')=='3'
assert Solution().smallestGoodBase('4681')=='8'
assert Solution().smallestGoodBase('1000000000000000000')=='999999999999999999'