#
# @lc app=leetcode.cn id=764 lang=python3
#
# [764] 最大加号标志
#
from typing import List
# @lc code=start
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        zeros={(x,y) for x,y in mines}
        f=[[n]*n for _ in range(n)]
        for i in range(n):
            #left
            count=0
            for j in range(n):
                if (i,j) in zeros:
                    count=0
                else:
                    count+=1
                f[i][j]=min(f[i][j],count)
            # right
            count=0
            for j in range(n-1,-1,-1):
                if (i,j) in zeros:
                    count=0
                else:
                    count+=1
                f[i][j]=min(f[i][j],count)
            
            # top
            count=0
            for j in range(n-1,-1,-1):
                if (j,i) in zeros:
                    count=0
                else:
                    count+=1
                f[j][i]=min(f[j][i],count)
            
            count=0
            for j in range(n):
                if (j,i) in zeros:
                    count=0
                else:
                    count+=1
                f[j][i]=min(f[j][i],count)
        return max(map(max,f))
# @lc code=end
n=3
mines=[[0,1]]
assert Solution().orderOfLargestPlusSign(n,mines)==1

n = 5
mines = [[4, 2]]
assert Solution().orderOfLargestPlusSign(n,mines)==2
n = 1
mines = [[0, 0]]
assert Solution().orderOfLargestPlusSign(n,mines)==0