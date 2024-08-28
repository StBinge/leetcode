#
# @lc app=leetcode.cn id=2050 lang=python3
# @lcpr version=30204
#
# [2050] 并行课程 III
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indeg=[0]*n
        prev2nxt=defaultdict(list)
        for prev,nxt in relations:
            prev-=1
            nxt-=1
            indeg[nxt]+=1
            prev2nxt[prev].append(nxt)
        
        lessons=[i for i,deg in enumerate(indeg) if deg==0]
        times=[0]*n
        ret=0
        while lessons:
            l=lessons.pop()
            nxt_time=times[l]+time[l]
            ret=max(ret,nxt_time)
            for nxt in prev2nxt[l]:
                times[nxt]=max(times[nxt],nxt_time)
                indeg[nxt]-=1
                if indeg[nxt]==0:
                    lessons.append(nxt)
        return ret
# @lc code=end
assert Solution().minimumTime(n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5])==12
assert Solution().minimumTime(n = 3, relations = [[1,3],[2,3]], time = [3,2,5])==8


#
# @lcpr case=start
# 3\n[[1,3],[2,3]]\n[3,2,5]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[1,5],[2,5],[3,5],[3,4],[4,5]]\n[1,2,3,4,5]\n
# @lcpr case=end

#

