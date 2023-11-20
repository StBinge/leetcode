#
# @lc app=leetcode.cn id=798 lang=python3
#
# [798] 得分最高的最小轮调
#
from typing import List
# @lc code=start
class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        L=len(nums)
        # Max_idx=L-1
        diff=[0]*L
        
        for i,n in enumerate(nums):
            low=(1+i)%L
            high=(L+i-n+1)%L
            diff[low]+=1
            diff[high]-=1
            if low>=high:
                diff[0]+=1
            # if n>=L:
            #     continue
            # # if n==0:
            # #     diff[0]+=1
            # #     continue
            # if n<=i:
            #     diff[0]+=1
            #     if i-n+1<L:
            #         diff[i-n+1]-=1
            #     if i+1<L:
            #         diff[i+1]+=1
            #     # diff[L-1+1]-=1
            # else:
            #     least_move=i+1
            #     most_move=L-1-n+least_move
            #     diff[least_move]+=1
            #     if most_move+1<L:
            #         diff[most_move+1]-=1
        
        ret=0
        cur_p=0
        max_p=0
        for i,k in enumerate(diff):
            cur_p+=k
            if cur_p>max_p:
                max_p=cur_p
                ret=i
        return ret


# @lc code=end

nums = [2,3,1,4,0]
assert Solution().bestRotation(nums)==3
nums=[1,3,0,2,4]
assert Solution().bestRotation(nums)==0