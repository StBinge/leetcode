#
# @lc app=leetcode.cn id=1563 lang=python3
#
# [1563] 石子游戏 V
#
from sbw import *
# @lc code=start
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n=len(stoneValue)
        max_l=[[0]*n for _ in range(n)]
        max_r=[[0]*n for _ in range(n)]
        f=[[0]*n for _ in range(n)]

        for left in range(n-1,-1,-1):
            max_l[left][left]=max_r[left][left]=stoneValue[left]
            i=left-1
            tot=stoneValue[left]
            suml=0
            for right in range(left+1,n):
                tot+=stoneValue[right]
                while i+1<right and (suml+stoneValue[i+1])*2<=tot:
                    suml+=stoneValue[i+1]
                    i+=1
                if left<=i:
                    f[left][right]=max(f[left][right],max_l[left][i])
                if i+1<right:
                    f[left][right]=max(f[left][right],max_r[i+2][right])
                if suml*2==tot:
                    f[left][right]=max(f[left][right],max_r[i+1][right])

                max_l[left][right]=max(max_l[left][right-1],tot+f[left][right])
                max_r[left][right]=max(max_r[left+1][right],tot+f[left][right])
        return f[0][-1]

# @lc code=end

assert Solution().stoneGameV([98,77,24,49,6,12,2,44,51,96])==330

assert Solution().stoneGameV([1,1,2])==3
assert Solution().stoneGameV([7,7,7,7,7,7,7])==28
assert Solution().stoneGameV(stoneValue = [6,2,3,4,5,5])==18