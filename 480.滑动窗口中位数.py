#
# @lc app=leetcode.cn id=480 lang=python3
#
# [480] 滑动窗口中位数
#
from typing import List
# @lc code=start
import heapq
class DualHeap:
    def __init__(self,k:int) -> None:
        self.small=[]
        self.large=[]
        self.k=k
        self.small_size=0
        self.large_size=0
        self.deleted={}
    
    def prune(self, queue):
        while queue:
            n=queue[0]
            if queue is self.small:
                n=-n
            if n in self.deleted:
                heapq.heappop(queue)
                self.deleted[n]-=1
                if self.deleted[n]==0:
                    del self.deleted[n]
            else:
                break
    
    def make_balance(self):
        if self.small_size>self.large_size+1:
            n=-heapq.heappop(self.small)
            self.small_size-=1
            heapq.heappush(self.large,n)
            self.large_size+=1
            self.prune(self.small)
        elif self.small_size<self.large_size:
            n=heapq.heappop(self.large)
            self.large_size-=1
            heapq.heappush(self.small,-n)
            self.small_size+=1
            self.prune(self.large)

    
    def insert(self,n):
        if not self.small_size or n<=-self.small[0]:
            heapq.heappush(self.small,-n)
            self.small_size+=1
        else:
            heapq.heappush(self.large,n)
            self.large_size+=1
        self.make_balance()

    def erase(self,n):
        cnt=self.deleted.get(n,0)+1
        self.deleted[n]=cnt
        if n<=-self.small[0]:
            self.small_size-=1
            if n==-self.small[0]:
                self.prune(self.small)
        else:
            self.large_size-=1
            if n==self.large[0]:
                self.prune(self.large)
        self.make_balance()
    
    def get_median(self):
        return -self.small[0] if self.k%2 else (-self.small[0]+self.large[0])/2

        


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        h=DualHeap(k)
        for n in nums[:k]:
            h.insert(n)
        ans=[h.get_median()]
        for i in range(k,len(nums)):
            h.erase(nums[i-k])
            h.insert(nums[i])
            ans.append(h.get_median())
        return ans
# @lc code=end

assert Solution().medianSlidingWindow([2147483647,1,2,3,4,5,6,7,2147483647],2)==[1073741824.0,1.5,2.5,3.5,4.5,5.5,6.5,1073741827.0]
assert Solution().medianSlidingWindow([1,3,-1,-3,5,3,6,7],3)==[1,-1,-1,3,5,6]