#
# @lc app=leetcode.cn id=1390 lang=python3
#
# [1390] 四因数
#
from sbw import *
# @lc code=start
import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        C=max(nums)
        C3=int(math.pow(C,1/3))
        is_prime=[True]*(C+1)
        primes=[]
        for i in range(2,C+1):
            if is_prime[i]:
                primes.append(i)
            for j in range(i*2,C+1,i):
                is_prime[j]=False
        
        f4={}
        for p in primes:
            if p**3<=C:
                f4[p**3]=1+p+p**2+p**3
        for i in range(len(primes)):
            p1=primes[i]
            if p1*p1>C:
                break
            for j in range(i+1,len(primes)):
                p2=primes[j]
                if p1*p2<=C:
                    f4[p1*p2]=1+p1+p2+p1*p2
                else:
                    break
        ret=0
        for n in nums:
            ret+=f4.get(n,0)
        return ret
# @lc code=end
assert Solution().sumFourDivisors([1,2,3,4,5])==0
assert Solution().sumFourDivisors([21,21])==64
assert Solution().sumFourDivisors([21,4,7])==32
