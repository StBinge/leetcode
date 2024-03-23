#
# @lc app=leetcode.cn id=1353 lang=python3
#
# [1353] 最多可以参加的会议数目
#
from sbw import *
# @lc code=start
import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        heap=[]
        start_time={}
        # end_time={}
        mi,ma=10**5,0
        for i,[s,e] in enumerate(events):
            start_time.setdefault(s,[]).append(i)
            # end_time.setdefault(e,[]).append(i)
            mi=min(mi,s)
            ma=max(ma,e)
        ret=0

        for day in range(mi,ma+1):
            while heap and heap[0]<day:
                heapq.heappop(heap)
            for i in start_time.get(day,[]):
                heapq.heappush(heap,events[i][1])
            if heap:
                ret+=1
                heapq.heappop(heap)
            
        return ret
        
# @lc code=end
assert Solution().maxEvents([[1,5],[1,5],[1,5],[2,3],[2,3]])==5
assert Solution().maxEvents([[1,2],[1,2],[3,3],[1,5],[1,5]])==5
assert Solution().maxEvents([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]])==7
assert Solution().maxEvents([[1,2],[2,3],[3,4],[1,2]])==4
assert Solution().maxEvents( [[1,2],[2,3],[3,4]])==3
