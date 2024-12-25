#
# @lc app=leetcode.cn id=LCR 146 lang=python3
# @lcpr version=30204
#
# [LCR 146] 螺旋遍历二维数组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def spiralArray(self, array: List[List[int]]) -> List[int]:
        if not array:
            return []
        R,C=len(array),len(array[0])
        ret=[]
        dirs=[
            [0,1],
            [1,0],
            [0,-1],
            [-1,0]
        ]
        dir=0
        r=c=0
        for i in range(R*C):
            ret.append(array[r][c])
            array[r][c]=None
            dr,dc=dirs[dir]
            nr,nc=r+dr,c+dc
            if 0<=nr<R and 0<=nc<C and array[nr][nc]!=None:
                r,c=nr,nc
            else:
                dir=(dir+1)%4
                r+=dirs[dir][0]
                c+=dirs[dir][1]

        return ret
# @lc code=end
assert Solution().spiralArray([[2,3]])==[2,3]
assert Solution().spiralArray([[1,2,3],[8,9,4],[7,6,5]])==[1,2,3,4,5,6,7,8,9]


#
# @lcpr case=start
# [[1,2,3],[8,9,4],[7,6,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]\n
# @lcpr case=end

#

