#
# @lc app=leetcode.cn id=3015 lang=python3
# @lcpr version=30204
#
# [3015] 按距离统计房屋对数目 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x>y:
            x,y=y,x
        if x+1>=y:
            return list(range((n-1)*2,-1,-2))
        
        difs=[0]*(n+1)
        def add(l,r):
            difs[l]+=2
            difs[r+1]-=2

        for i in range(1,n):
            if i<=x:
                k=(x+y+1)//2
                add(1,k-i)
                add(x-i+2,x-i+y-k)
                add(x-i+1,n-y+x-i+1)
            elif i<(x+y)//2:
                k=i+(y-x+1)//2
                add(1,k-i)
                add(i-x+2,i-x+y-k)
                add(i-x+1,i-x+1+n-y)
            else:
                add(1,n-i)
            
        ret=[0]*n
        cur=0
        for i in range(1,n):
            cur+=difs[i]
            ret[i-1]=cur
        return ret

                


# @lc code=end
assert Solution().countOfPairs(n = 4, x = 1, y = 1)==[6,4,2,0]
assert Solution().countOfPairs(n = 5, x = 2, y = 4)==[10,8,2,0,0]
assert Solution().countOfPairs(n = 3, x = 1, y = 3)==[6,0,0]


#
# @lcpr case=start
# 3\n1\n3\n
# @lcpr case=end

# @lcpr case=start
# 5\n2\n4\n
# @lcpr case=end

# @lcpr case=start
# 4\n1\n1\n
# @lcpr case=end

#

