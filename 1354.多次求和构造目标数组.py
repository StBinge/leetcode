#
# @lc app=leetcode.cn id=1354 lang=python3
#
# [1354] 多次求和构造目标数组
#
from sbw import *
# @lc code=start
import heapq
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target)==1 and target[0]!=1:
            return False
        heap=[]
        s=0
        for n in target:
            heapq.heappush(heap,-n)
            s+=n

        while heap:
            x=-heapq.heappop(heap)
            if x==1:
                return True
            y=-heap[0]
            left=s-x
            if y==1:
                k=(x-y+left-1)//left
            else:
                k=(x-y)//left+1
            x-=k*left
            if x<1:
                return False
            heapq.heappush(heap,-x)
            s=left+x
        return True
# @lc code=end
assert Solution().isPossible([2])==False
assert Solution().isPossible([8,5])
assert Solution().isPossible([1,1,10])==False
assert Solution().isPossible([2,900000002])==False
assert Solution().isPossible([1,1,2])==False
assert Solution().isPossible([1,1000000000])
assert Solution().isPossible([1,1,1,2])==False
assert Solution().isPossible([9,3,5])
