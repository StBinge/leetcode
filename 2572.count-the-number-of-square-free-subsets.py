#
# @lc app=leetcode.cn id=2572 lang=python3
# @lcpr version=30204
#
# [2572] 无平方子集计数
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        cnt1=cnt[1]
        del cnt[1]
        primes = [2, 3, 5, 7, 11, 13,17,19,23,29]
        mod=10**9+7
        pmasks=[]
        nums=[]
        for n in cnt.keys():
            m=0
            for i,p in enumerate(primes):
                if n%(p*p)==0:
                    break
                if n%p==0:
                    m|=1<<i
            else:
                nums.append(n)
                pmasks.append(m)
        
        N=len(nums)
        M=len(primes)
        Mask=(1<<M)-1
        f=[0]*(1<<M)
        f[0]=pow(2,cnt1,mod)
        for i,n in enumerate(nums):
            mask=pmasks[i]
            j=sub=Mask^mask
            while True:
                f[mask|j]=(f[mask|j]+f[j]*cnt[n])%mod
                j=(j-1)&sub
                if j==sub: break
        return (sum(f)-1)%mod

# @lc code=end

assert Solution().squareFreeSubsets([1,2,6,15,7,19,6,29,28,24,21,25,25,18,9,6,20,21,8,24,14,19,24,28,30,27,13,21,1,23,13,29,24,29,18,7]) == 9215
assert Solution().squareFreeSubsets([8,11,17,2,25,29,21,20,4,22]) == 39
assert Solution().squareFreeSubsets([1]) == 1
assert Solution().squareFreeSubsets([3, 4, 4, 5,5]) == 5
assert Solution().squareFreeSubsets([3, 4, 4, 5]) == 3


#
# @lcpr case=start
# [3,4,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
