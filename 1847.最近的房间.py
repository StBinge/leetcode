#
# @lc app=leetcode.cn id=1847 lang=python3
#
# [1847] 最近的房间
#
from sbw import *
# @lc code=start
from sortedcontainers import SortedList
class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        rooms.sort(key=lambda x:-x[1])
        N=len(queries)
        sorted_qid=sorted(range(N),key=lambda x:-queries[x][1])
        ret=[-1]*N
        idx=0
        M=len(rooms)
        candidates=SortedList()
        for qid in sorted_qid:
            prefer,limit=queries[qid]
            while idx<M and rooms[idx][1]>=limit:
                candidates.add(rooms[idx][0])
                idx+=1
            p=candidates.bisect_left(prefer)
            dif=1e9
            if p<len(candidates):
                dif=candidates[p]-prefer
                ret[qid]=candidates[p]
            if p>0:
                if prefer-candidates[p-1]<=dif:
                    ret[qid]=candidates[p-1]
        return ret
# @lc code=end
assert Solution().closestRoom(rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]])==[2,1,3]
assert Solution().closestRoom(rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]])==[3,-1,3]
