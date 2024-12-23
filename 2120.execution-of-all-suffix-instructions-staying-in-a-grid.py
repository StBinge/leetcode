#
# @lc app=leetcode.cn id=2120 lang=python3
# @lcpr version=30204
#
# [2120] 执行所有后缀指令
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        N=len(s)
        fx=defaultdict(int)
        fy=defaultdict(int)
        dirs={
            'L':[-1,0],
            'R':[1,0],
            'U':[0,-1],
            'D':[0,1],
        }
        y,x=startPos
        for c in s:
            dx,dy=dirs[c]
            x+=dx
            y+=dy
        
        ret=[0]*N
        for i in range(N-1,-1,-1):
    
            fx[x]=fy[y]=N-i
            dx,dy=dirs[s[i]]
            x-=dx
            y-=dy
            xx,yy=x-startPos[1],y-startPos[0]
            cnt=max(fx[xx-1],fx[xx+n],fy[yy-1],fy[yy+n])
            ret[i]=N-i-cnt
        return ret

# @lc code=end
assert Solution().executeInstructions(n = 3, startPos = [0,1], s = "RRDDLU")==[1,5,4,3,1,0]


#
# @lcpr case=start
# 3\n[0,1]\n"RRDDLU"\n
# @lcpr case=end

# @lcpr case=start
# 2\n[1,1]\n"LURD"\n
# @lcpr case=end

# @lcpr case=start
# 1\n[0,0]\n"LRUD"\n
# @lcpr case=end

#

