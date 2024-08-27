#
# @lc app=leetcode.cn id=1654 lang=python3
#
# [1654] 到家的最少跳跃次数
#
from sbw import *
# @lc code=start
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        q=[[x,0,0,0]]
        vis=set(forbidden)
        # back_vis=set()
        Max=max(max(forbidden)+a,x)+b
        while q:
            _,step,pos,dir=heapq.heappop(q)
            if pos==x:
                return step
            nxt_pos=pos+a
            if nxt_pos not in vis and nxt_pos<=Max:
                heapq.heappush(q,[abs(x-nxt_pos),step+1,nxt_pos,1])
                vis.add(nxt_pos)
            if dir==1:
                nxt_pos=pos-b
                if nxt_pos<0 or nxt_pos in vis or -nxt_pos in vis:
                    continue
                heapq.heappush(q,[abs(x-nxt_pos),step+1,nxt_pos,-1])
                vis.add(-nxt_pos)
        return -1
# @lc code=end
assert Solution().minimumJumps([162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98],29,98,80)==121
assert Solution().minimumJumps(forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7)==2
assert Solution().minimumJumps(forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11)==-1
assert Solution().minimumJumps(forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9)==3
