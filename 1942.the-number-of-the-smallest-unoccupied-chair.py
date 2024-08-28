#
# @lc app=leetcode.cn id=1942 lang=python3
# @lcpr version=30204
#
# [1942] 最小未被占据椅子的编号
#
from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        arrive_times=sorted([[t[0],i] for i,t in enumerate(times)])
        leave_times=sorted([[t[1],i] for i,t in enumerate(times)])
        
        tot = 0
        available = []
        leave_idx=0
        N=len(times)
        seats=defaultdict(int)
        for arrive,idx in arrive_times:
            while leave_idx<N and leave_times[leave_idx][0]<=arrive:
                sid=leave_times[leave_idx][1]
                heapq.heappush(available,seats[sid])
                leave_idx+=1
            if not available:
                available.append(tot)
                tot += 1
            take = heapq.heappop(available)
            if idx == targetFriend:
                return take
            seats[idx]=take

# @lc code=end
assert Solution().smallestChair([[33889,98676],[80071,89737],[44118,52565],[52992,84310],[78492,88209],[21695,67063],[84622,95452],[98048,98856],[98411,99433],[55333,56548],[65375,88566],[55011,62821],[48548,48656],[87396,94825],[55273,81868],[75629,91467]],6) == 2
assert Solution().smallestChair(times = [[3,10],[1,5],[2,6]], targetFriend = 0) == 2
assert Solution().smallestChair(times=[[1, 4], [2, 3], [4, 6]], targetFriend=1) == 1


#
# @lcpr case=start
# [[1,4],[2,3],[4,6]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[3,10],[1,5],[2,6]]\n0\n
# @lcpr case=end

#
