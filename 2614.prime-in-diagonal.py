#
# @lc app=leetcode.cn id=2614 lang=python3
# @lcpr version=30204
#
# [2614] 对角线上的质数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        cache={}
        N=len(nums)        
        ret=0

        def is_prime(x):
            i=2
            while i*i<=x:
                if x%i==0:
                    return False
                i+=1
            return True
        
        for i in range(N):
            n=nums[i][i]
            if n>1 and n>ret and cache.setdefault(n,is_prime(n)):
                ret=max(ret,n)
            n=nums[i][N-i-1]
            if n>1 and n>ret and cache.setdefault(n,is_prime(n)):
                ret=max(ret,n)
        return ret


# @lc code=end
assert Solution().diagonalPrime()


#
# @lcpr case=start
# [[1,2,3],[5,6,7],[9,10,11]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[5,17,7],[9,11,10]]\n
# @lcpr case=end

#

