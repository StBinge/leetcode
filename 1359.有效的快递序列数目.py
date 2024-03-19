#
# @lc app=leetcode.cn id=1359 lang=python3
#
# [1359] 有效的快递序列数目
#

# @lc code=start
class Solution:
    def countOrders(self, n: int) -> int:
        ret=1
        Mod=10**9+7
        for i in range(2,2*n+1,2):
            ret*=(i*(i-1))//2
            ret%=Mod
        return ret
# @lc code=end
assert Solution().countOrders(3)==90
assert Solution().countOrders(2)==6
assert Solution().countOrders(1)==1
