#
# @lc app=leetcode.cn id=768 lang=python3
#
# [768] 最多能完成排序的块 II
#
from typing import List
# @lc code=start
# import bisect
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        L=len(arr)
        # vals=[]
        # least_bigger=[-1]*L
        # least_bigger[-1]=L
        # vals.append(arr[-1])
        # for i in range(L-2,-1,-1):
        stack=[]
        for n in arr:
            if not stack or stack[-1]<=n:
                stack.append(n)
            else:
                head=stack.pop()
                while stack and stack[-1]>n:
                    stack.pop()
                stack.append(head)
        return len(stack)
            
# @lc code=end
arr = [5,4,3,2,1]
assert Solution().maxChunksToSorted(arr)==1

arr = [2,1,3,4,4]
assert Solution().maxChunksToSorted(arr)==4

