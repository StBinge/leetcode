#
# @lc app=leetcode.cn id=650 lang=python3
#
# [650] 只有两个键的键盘
#

# @lc code=start
from functools import lru_cache
class Solution:
    def minSteps(self, n: int) -> int:
        ret=0
        i=2
        while i*i<=n:
            while n%i==0:
                ret+=i
                n//=i
            i+=1
        if n>1:
            ret+=n
        return ret

# @lc code=end
assert Solution().minSteps(5)==5
assert Solution().minSteps(3)==3
assert Solution().minSteps(1)==0
