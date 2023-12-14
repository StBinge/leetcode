#
# @lc app=leetcode.cn id=975 lang=python3
#
# [975] 奇偶跳
#
from sbw import *
# @lc code=start
from sortedcontainers import SortedList
import bisect
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        L=len(arr)
        def make(orders:list):
            nonlocal L
            stack=[]
            ans=[None]*L
            for i in orders:
                while stack and i>stack[-1]:
                    ans[stack.pop()]=i
                stack.append(i)
            return ans
        
        asc_sort=sorted(range(L),key=arr.__getitem__)
        odd_next=make(asc_sort)
        dec_sort=sorted(range(L),key=lambda i:-arr[i])
        even_next=make(dec_sort)
        odd=[False]*L
        even=[False]*L
        odd[-1]=even[-1]=True
        ret=1
        for i in range(L-2,-1,-1):
            if odd_next[i] and even[odd_next[i]]:
                odd[i]=True
                ret+=1
            if even_next[i] and odd[even_next[i]]:
                even[i]=True
        return ret

# @lc code=end
arr=[5,1,3,4,2]
assert Solution().oddEvenJumps(arr)==3

arr=[2,3,1,1,4]
assert Solution().oddEvenJumps(arr)==3

arr=[10,13,12,14,15]
assert Solution().oddEvenJumps(arr)==2
