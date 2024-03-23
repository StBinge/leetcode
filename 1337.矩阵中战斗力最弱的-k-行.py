#
# @lc app=leetcode.cn id=1337 lang=python3
#
# [1337] 矩阵中战斗力最弱的 K 行
#
from sbw import *
# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        R,C=len(mat),len(mat[0])
        counter={}
        for row in range(R):
            l,r=0,C
            while l<r:
                mid=(l+r)>>1
                if mat[row][mid]==1:
                    l=mid+1
                else:
                    r=mid
            counter.setdefault(l,[]).append(row)
        ret=[]
        for cnt in sorted(counter.keys()):
            appended=min(len(counter[cnt]),k)
            ret.extend(counter[cnt][:appended])
            k-=appended
            if k==0:
                return ret
# @lc code=end
assert Solution().kWeakestRows(mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2)==[0,2]
assert Solution().kWeakestRows(mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3)==[2,0,3]
