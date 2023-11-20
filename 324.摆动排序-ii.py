#
# @lc app=leetcode.cn id=324 lang=python3
#
# [324] 摆动排序 II
#
from typing import List
# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partion(nums,l,r):
            if l==r:
                return l
            pivot=nums[r]
            i=l
            while l<r:
                if nums[l]<pivot:
                    nums[i],nums[l]=nums[l],nums[i]
                    i+=1
                l+=1
            nums[i],nums[r]=nums[r],nums[i]
            return i
        def quick_sort(nums,l,r,index):
            if l==r:
                return nums[l]
            pi=partion(nums,l,r)
            if pi==index:
                return nums[pi]
            if pi<index:
                return quick_sort(nums,pi+1,r,index)
            else:
                return quick_sort(nums,l,pi-1,index)
        
        mid=(len(nums)+1)//2
        mid_val=quick_sort(nums,0,len(nums)-1,mid)
        N=len(nums)
        left,right,idx=0,N-1,0
        while idx<right:
            if nums[idx]>mid_val:
                nums[idx],nums[right]=nums[right],nums[idx]
                right-=1
            elif nums[idx]<mid_val:
                nums[idx],nums[left]=nums[left],nums[idx]
                left+=1
                idx+=1
            else:
                idx+=1
        temp=nums.copy()
        cnt=0
        left_end,right_end=mid-1,N-1
        while cnt<N:
            nums[cnt]=temp[left_end]
            left_end-=1
            cnt+=1
            if cnt<N:
                nums[cnt]=temp[right_end]
                right_end-=1
                cnt+=1
        


# @lc code=end
nums=[4,5,1,2,1,5,0,2,0,6,1,5,1,5,3,6,1,3,2,5,2,9,3,8,6,8,5,8,0,7,3,6,4,9,2,4,1,8,5,8,4,8,0,7,1,9,0,6,2,5,0,5,1,6,3,7,6,9,4,6,4,9,0,8,5,8,1,2,0,8,7,8,2,6,0,7,3,5,2,8,4,7,1,7,3,6,0,2,0,7,1,2,1,9,6,9,6,9,1,5]
Solution().wiggleSort(nums)
print(nums)


nums=[1]
Solution().wiggleSort(nums)
print(nums)

nums=[1,5,1,1,6,4]
Solution().wiggleSort(nums)
print(nums)

nums=[1,3,2,2,3,1]
Solution().wiggleSort(nums)
print(nums)