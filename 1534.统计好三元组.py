#
# @lc app=leetcode.cn id=1534 lang=python3
#
# [1534] 统计好三元组
#
from sbw import *


# @lc code=start
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        Max=max(arr)+max(a,b,c)+1
        seg=[0]*(Max+1)
        def low_bit(x):
            return x & (-x)
        def add(x):
            while x<=Max:
                seg[x]+=1
                x+=low_bit(x)
        def query(x):
            ret=0
            while x:
                ret+=seg[x]
                x-=low_bit(x)
            return ret
        
        ret=0
        N=len(arr)
        # for i in range(N):
        #     x=arr[i]
        #     for j in range(i+1,N):
        #         y=arr[j]
        #         for k in range(j+1,N):
        #             z=arr[k]
        #             if abs(x-y)<=a and abs(y-z)<=b and abs(x-z)<=c:
        #                 print((i,j,k))
        for i in range(N):
            x=arr[i]
            for j in range(i+1,N):
                y=arr[j]
                if abs(x-y)>b:
                    continue
                l1,r1=x-a,x+a
                l2,r2=y-c,y+c
                l=max(0,l1,l2)
                r=min(r1,r2,Max)
                if l>r:
                    continue
                cnt=query(r+1)-query(l)
                ret+=cnt
            add(x+1)
        return ret

# @lc code=end
assert Solution().countGoodTriplets([4,9,9,8,9,5,3,7],1,3,0) == 3
assert Solution().countGoodTriplets(arr=[3, 0, 1, 1, 9, 7], a=7, b=2, c=3) == 4
