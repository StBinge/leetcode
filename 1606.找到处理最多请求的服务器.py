#
# @lc app=leetcode.cn id=1606 lang=python3
#
# [1606] 找到处理最多请求的服务器
#
from sbw import *


# @lc code=start
from sortedcontainers import SortedList
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        cnt = [0] * k
        # end_time = [-1] * k
        busy=[] # [end_time,sid]
        available=list(range(k))
        for i, (arrive, work) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= arrive:
                _,sid=heapq.heappop(busy)
                heapq.heappush(available,i+(sid-i)%k)
            if not available:
                continue
            sid=heapq.heappop(available)%k
            heapq.heappush(busy,(arrive+work,sid))
            cnt[sid]+=1
 
        ret = []
        max_cnt = 0
        for i, c in enumerate(cnt):
            if c > max_cnt:
                ret = [i]
                max_cnt = c
            elif c == max_cnt:
                ret.append(i)
        return ret


# @lc code=end
assert Solution().busiestServers(k = 3, arrival = [1,2,3,4,8,9,10], load = [5,2,10,3,1,2,2]) == [1]
assert Solution().busiestServers(k = 3, arrival = [1,2,3], load = [10,12,11]) == [0,1,2]
assert Solution().busiestServers(k=3, arrival=[1, 2, 3, 4], load=[1, 2, 1, 2]) == [0]
assert Solution().busiestServers(
    k=3, arrival=[1, 2, 3, 4, 5], load=[5, 2, 3, 3, 3]
) == [1]
