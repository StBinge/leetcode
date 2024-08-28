#
# @lc app=leetcode.cn id=1508 lang=python3
#
# [1508] 子数组和排序后的区间和
#
from sbw import *
# @lc code=start
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        Mods=10**9+7
        L=len(nums)
        p_sum=[0]
        pp_sum=[0]
        for n in nums:
            p_sum.append(p_sum[-1]+n)
            pp_sum.append(pp_sum[-1]+p_sum[-1])
        def count(x):
            cnt=0
            idx=1
            for i in range(L):
                while idx<=L and p_sum[idx]-p_sum[i]<=x:
                    idx+=1
                idx-=1
                cnt+=idx-i
            return cnt
        
        def get_kth(k):
            l,r=0,p_sum[-1]
            while l<r:
                mid=(l+r)>>1
                cnt=count(mid)
                if cnt>=k:
                    r=mid
                else:
                    l=mid+1
            return r
        
        def get_k_sum(k):
            x=get_kth(k)
            index=1
            cnt=0
            ret=0
            for i in range(L):
                while index<=L and p_sum[index]-p_sum[i]<x:
                    index+=1
                index-=1
                cnt+=index-i
                ret+=pp_sum[index]-pp_sum[i]-p_sum[i]*(index-i)
            return ret+(k-cnt)*x
        
        right_sum=get_k_sum(right)
        left_sum=get_k_sum(left-1)
        ret=(right_sum-left_sum)%Mods
        return ret

# @lc code=end
assert Solution().rangeSum([7,5,8,5,6,4,3,3],8,2,6)==23
assert Solution().rangeSum(nums = [1,2,3,4], n = 4, left = 3, right = 4)==6
assert Solution().rangeSum(nums = [1,2,3,4], n = 4, left = 1, right = 5)==13
