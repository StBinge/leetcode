#
# @lc app=leetcode.cn id=1001 lang=python3
#
# [1001] 网格照明
#
from sbw import *
# @lc code=start
class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        rows=Counter()
        cols=Counter()
        dig_1=Counter()
        # dig_1=Counter()
        dig_2=Counter()
        
        lamps=set(map(tuple,lamps))
        def turn(r,c, flag):
            rows[r]+=flag
            cols[c]+=flag
            dig_1[r-c]+=flag
            dig_2[r+c]+=flag

        for r,c in lamps:
            turn(r,c,1)

        ret=[0]*len(queries)
        for i,[r,c] in enumerate(queries):
            if rows[r]>0 or cols[c]>0 or dig_1[r-c]>0 or dig_2[r+c]>0:
                ret[i]=1
            for x in [r-1,r,r+1]:
                for y in [c-1,c,c+1]:
                    if (x,y) in lamps:
                        turn(x,y,-1)
                        lamps.remove((x,y))
        return ret
# @lc code=end
n = 6
lamps = [[2,5],[4,2],[0,3],[0,5],[1,4],[4,2],[3,3],[1,0]]
queries = [[4,3],[3,1],[5,3],[0,5],[4,4],[3,3]]
ret=[1,0,1,1,0,1]
assert Solution().gridIllumination(n,lamps,queries)==ret


n = 5
lamps = [[0,0],[1,0]]
queries = [[1,1],[1,1]]
ret=[1,0]
assert Solution().gridIllumination(n,lamps,queries)==ret

n=5
lamps=[[0,0],[0,1],[0,4]]
queries=[[0,0],[0,1],[0,2]]
ret=[1,1,1]
assert Solution().gridIllumination(n,lamps,queries)==ret

n = 5
lamps = [[0,0],[0,4]]
queries = [[0,4],[0,1],[1,4]]
ret=[1,1,0]
assert Solution().gridIllumination(n,lamps,queries)==ret

n = 5
lamps = [[0,0],[4,4]]
queries = [[1,1],[1,1]]
ret=[1,1]
assert Solution().gridIllumination(n,lamps,queries)==ret
n = 5
lamps = [[0,0],[4,4]]
queries = [[1,1],[1,0]]
ret=[1,0]
assert Solution().gridIllumination(n,lamps,queries)==ret
