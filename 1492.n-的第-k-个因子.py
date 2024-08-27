#
# @lc app=leetcode.cn id=1492 lang=python3
#
# [1492] n 的第 k 个因子
#

# @lc code=start
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        fac=1
        while fac*fac<=n:
            if n%fac==0:
                k-=1
                if k==0:
                    return fac
            fac+=1
        fac-=1
        if fac*fac==n:
            fac-=1
        while fac:
            if n%fac==0:
                k-=1
                if k==0:
                    return n//fac
            fac-=1
        return -1
    
# @lc code=end
assert Solution().kthFactor(4,4)==-1
assert Solution().kthFactor(7,2)==7
assert Solution().kthFactor(12,3)==3
