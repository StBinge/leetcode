#
# @lc app=leetcode.cn id=793 lang=python3
#
# [793] 阶乘函数后 K 个零
#

# @lc code=start
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def zeta(n:int):
            ret=0
            while n>0:
                n//=5
                ret+=n
            return ret
        left=0
        right=5*k+1
        while left<right:
            mid=(left+right)//2
            z=zeta(mid)
            if z==k:
                return 5
            elif z<k:
                left=mid+1
            else:
                right=mid-1
        return 0
# @lc code=end
assert Solution().preimageSizeFZF(0)==5
assert Solution().preimageSizeFZF(5)==0
assert Solution().preimageSizeFZF(3)==5
