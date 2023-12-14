#
# @lc app=leetcode.cn id=923 lang=python3
#
# [923] 三数之和的多种可能
#
from sbw import *
# @lc code=start
from math import comb
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ret=0
        Mod=10**9+7
        counters=Counter(arr)
        nums=sorted(counters.keys())
        for i,n in enumerate(nums):
            T=target-n
            j,k=i,len(nums)-1
            while j<=k:
                s=nums[j]+nums[k]
                if s<T:
                    j+=1
                elif s>T:
                    k-=1
                else:
                    if i<j<k:
                        ret+=counters[n]*counters[nums[j]]*counters[nums[k]]
                    elif i==j<k:
                        ret+=comb(counters[n],2)*counters[nums[k]]
                    elif i<j==k:
                        ret+=comb(counters[nums[j]],2)*counters[n]
                    else:
                        ret+=comb(counters[nums[j]],3)
                    j+=1
                    k-=1
                    ret%=Mod
        return ret
                    
                    
        return ret

# @lc code=end
arr = [1,1,2,2,2,2]
target = 5
ret=12
assert Solution().threeSumMulti(arr,target)==12

arr = [1,1,2,2,3,3,4,4,5,5]
target = 8
ret=20
assert Solution().threeSumMulti(arr,target)==20
