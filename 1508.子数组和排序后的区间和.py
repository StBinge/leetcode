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
            p_sum.append(n+p_sum[-1])
            pp_sum.append(p_sum[-1]+pp_sum[-1])

        def count(x:int):
            idx=1
            cnt=0
            for i in range(L):
                while idx<=L and p_sum[idx]-p_sum[i]<=x:
                    idx+=1
                idx-=1
                cnt+=idx-i
            return cnt
        
        def get_kth(k):
            left,right=0,p_sum[-1]
            while left<right:
                mid=(left+right)>>1
                cnt=count(mid)
                if cnt<k:
                    left=mid+1
                else:
                    right=mid
            return left
        
        def get_sum(k):
            x=get_kth(k)
            cnt=0
            idx=1
            ret=0
            for i in range(L):
                while idx<=L and p_sum[idx]-p_sum[i]<x:
                    idx+=1
                idx-=1
                cnt+=idx-i
                ret+=pp_sum[idx]-pp_sum[i] - (idx-i)*p_sum[i]
            return ret+(k-cnt)*x
        
        left_s=get_sum(left-1)
        right_s=get_sum(right)

        return (right_s-left_s)%Mods

# @lc code=end
assert Solution().rangeSum([7,5,8,5,6,4,3,3],8,2,6)==23
assert Solution().rangeSum(nums = [1,2,3,4], n = 4, left = 3, right = 4)==6
assert Solution().rangeSum(nums = [1,2,3,4], n = 4, left = 1, right = 5)==13
