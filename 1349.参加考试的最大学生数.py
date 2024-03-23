#
# @lc app=leetcode.cn id=1349 lang=python3
#
# [1349] 参加考试的最大学生数
#
from sbw import *
# @lc code=start
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        R,C=len(seats),len(seats[0])
        invalids=[]
        for row in seats:
            mask=0
            for c in row:
                mask=(mask<<1)+int(c=='#')
            invalids.append(mask)



        @cache
        def dfs(rid,pre_mask):
            if rid==R:
                return 0

            ret=0
            invaid=invalids[rid] | (pre_mask)>>1 | (pre_mask<<1)
            valid=((1<<C)-1) & (~invaid)
            s=valid
            while s:              
                ret=max(ret,str(s).count('1')+dfs(rid+1,s))
                s=(s-1) * valid
            return max(ret,str(s).count('1')+dfs(rid+1,s))
        
        ret= dfs(0,0)
        return ret

# @lc code=end
assert Solution().maxStudents([["#",".","#","#",".","#"],
              [".","#","#","#","#","."],
              ["#",".","#","#",".","#"]])==4
