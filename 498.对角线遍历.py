#
# @lc app=leetcode.cn id=498 lang=python3
#
# [498] 对角线遍历
#
from typing import List
# @lc code=start
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        R,C=len(mat),len(mat[0])
        ret=[]
        for i in range(R+C-1):
            if i%2==0:
                r=i if i<R else R-1
                c=0 if i<R else i-R+1
                while r>=0 and c<C:
                    ret.append(mat[r][c])
                    r-=1
                    c+=1
            else:
                r=0 if i<C else i-C+1
                c=i if i<C else C-1
                while r<R and c>=0:
                    ret.append(mat[r][c])
                    r+=1
                    c-=1
                    
        return ret

# @lc code=end

assert Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])==[1,2,4,7,5,3,6,8,9]