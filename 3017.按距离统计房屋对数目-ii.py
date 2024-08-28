#
# @lc app=leetcode.cn id=3017 lang=python3
#
# [3017] 按距离统计房屋对数目 II
#
from sbw import *
# @lc code=start
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:

        if x>y:
            x,y=y,x
        if x+1>=y:
            return list(range((n-1)*2,-1,-2))
        
        diff=[0]*(n+1)
        def add(l,r):
            diff[l]+=2
            diff[r+1]-=2
        
        for i in range(1,n):
            if i<=x:
                k=(x+y+1)//2
                # i<j<=k
                add(1,k-i)
                # k<j<y
                left=x-i+2
                right=y-k-2+left # y+x-i-k
                add(left,right)
                # j>=y
                left=x-i+1
                right=n-y+left
                add(left,right)
            elif i<(x+y-1)/2:
                k=i+(y-x+1)//2
                # i<j<=k
                add(1,k-i)
                # k<j<y
                left=i-x+2
                right=y-k-2+left
                add(left,right)
                # j>=y
                left=i-x+1
                right=n-y+left
                add(left,right)
            else:
                add(1,n-i)

        return list(accumulate(diff))[1:]


# @lc code=end
assert Solution().countOfPairs(6,1,5)==[12,14,4,0,0,0]
assert Solution().countOfPairs(3,1,3)==[6,0,0]
