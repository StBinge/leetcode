#
# @lc app=leetcode.cn id=1482 lang=python3
#
# [1482] 制作 m 束花所需的最少天数
#
from sbw import *
# @lc code=start
# from sortedcontainers import SortedList
class LinkNode:
    def __init__(self,val:int,next:'LinkNode') -> None:
        self.val=val
        self.next=next

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        
        left,right=min(bloomDay),max(bloomDay)
        def can_make(day):
            ret=flowers=0
            for d in bloomDay:
                if d <=day:
                    flowers+=1
                    if flowers==k:
                        ret+=1
                        if ret==m:
                            break
                        flowers=0
                else:
                    flowers=0
            return ret==m
        
        while left<right:
            mid=(left+right)//2
            if can_make(mid):
                right=mid
            else:
                left=mid+1
        return right
# @lc code=end  

assert Solution().minDays(bloomDay = [1,10,2,9,3,8,4,7,5,6], m = 4, k = 2)==9
assert Solution().minDays(bloomDay = [1000000000,1000000000], m = 1, k = 1)==1000000000
assert Solution().minDays(bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3)==12
assert Solution().minDays(bloomDay = [1,10,3,10,2], m = 3, k = 2)==-1
assert Solution().minDays(bloomDay = [1,10,3,10,2], m = 3, k = 1)==3