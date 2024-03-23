#
# @lc app=leetcode.cn id=1301 lang=python3
#
# [1301] 最大得分的路径数目
#
from sbw import *
# @lc code=start
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        N=len(board)
        Mod=10**9+7
        f=[[[-1,0] for _ in range(N)] for _ in range(N)]
        f[0][0]=[0,1]

        def update(r,c,nr,nc):
            char=board[nr][nc]
            if char=='X':
                return
            if char=='S':
                char='0'
            val=f[r][c][0]+int(char)
            if val>f[nr][nc][0]:
                f[nr][nc][0]=val
                f[nr][nc][1]=f[r][c][1]
            elif val==f[nr][nc][0]:
                f[nr][nc][1]+=f[r][c][1] 

        for r in range(N):
            for c in range(N):
                if f[r][c][0]<0:
                    continue
                if c+1<N:
                    update(r,c,r,c+1)
                if r+1<N:
                    update(r,c,r+1,c)
                if r+1<N and c+1<N:
                    update(r,c,r+1,c+1)
                
        val,cnt=f[-1][-1]
        if val<0:
            return [0,0]
        return [val,cnt%Mod]



                
# @lc code=end

assert Solution().pathsWithMaxScore(["E11345","X452XX","3X43X4","422812","284522","13422S"])==[34,3]
assert Solution().pathsWithMaxScore(["E11","XXX","11S"])==[0,0]
assert Solution().pathsWithMaxScore(board = ["E12","1X1","21S"])==[4,2]
assert Solution().pathsWithMaxScore(board = ["E23","2X2","12S"])==[7,1]