#
# @lc app=leetcode.cn id=1240 lang=python3
#
# [1240] 铺瓷砖
#

# @lc code=start
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        matrix=[[False]*m for _ in range(n)]
        ret=m*n+1

        def set_flag(x,y,k,flag):
            for i in range(k):
                for j in range(k):
                    # if matrix[x+i][y+i]==flag:
                    #     return False
                    matrix[x+i][y+j]=flag
            # return True
        
        def can_set(x,y,k):
            for i in range(k):
                for j in range(k):
                    if matrix[i+x][j+y]:
                        return False
            return True

        def dfs(x,y,cnt):
            nonlocal ret
            if cnt>ret:
                return
            if x==n:
                ret=cnt
                return
            if y==m:
                dfs(x+1,0,cnt)
                return
            if matrix[x][y]:
                dfs(x,y+1,cnt)
                return
            vert=n-x
            hori=m-y
            l=min(vert,hori)
            for k in range(l,0,-1):
                if can_set(x,y,k)==False:
                    continue
                set_flag(x,y,k,True)
                dfs(x,y+k,cnt+1)
                set_flag(x,y,k,False)

        dfs(0,0,0)
        return ret
# @lc code=end
assert Solution().tilingRectangle(11,13)==6
assert Solution().tilingRectangle(2,3)==3
assert Solution().tilingRectangle(5,8)==5
