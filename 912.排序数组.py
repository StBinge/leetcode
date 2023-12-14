#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#
from sbw import *
# @lc code=start
import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(heap:list,root:int,hlen:int):
            p=root
            while p*2+1<hlen:
                l,r=2*p+1,2*p+2
                if r<hlen and heap[r]>heap[l]:
                    nxt=r
                else:
                    nxt=l
                if heap[p]<heap[nxt]:
                    heap[p],heap[nxt]=heap[nxt],heap[p]
                    p=nxt
                else:
                    break

        l=len(nums)
        for i in range(l-1,-1,-1):
            heapify(nums,i,l)

        for i in range(l-1,-1,-1):
            nums[i],nums[0]=nums[0],nums[i]
            heapify(nums,0,i)
        return nums
# @lc code=end
nums = [5,2,3,1]
ret=[1,2,3,5]
assert Solution().sortArray(nums)==ret
pass