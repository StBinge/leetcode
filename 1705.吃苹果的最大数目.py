#
# @lc app=leetcode.cn id=1705 lang=python3
#
# [1705] 吃苹果的最大数目
#
from sbw import *
# @lc code=start
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap=[]
        ret=0
        N=len(apples)
        for i in range(N):
            a,d=apples[i],days[i]
            heapq.heappush(heap,[i+d-1,a])
            while heap and  (heap[0][0]<i or heap[0][1]==0):
                heapq.heappop(heap)
            if heap:
                heap[0][1]-=1
                ret+=1
        end=N
        while heap:            
            day,a=heapq.heappop(heap)
            if day<end:
                continue
            eat=min(a,day-end+1)
            ret+=eat
            end+=eat
        return ret


# @lc code=end
assert Solution().eatenApples(apples = [1,2,3,5,2], days = [3,2,1,4,2])==7
assert Solution().eatenApples([5,2,3],[6,9,10])==10
assert Solution().eatenApples(apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2])==5
