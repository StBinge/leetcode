#
# @lc app=leetcode.cn id=1534 lang=python3
#
# [1534] 统计好三元组
#
from sbw import *


# @lc code=start
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        Max=max(arr)+1
        seg=[0]*(Max+1)
        def low_bit(x):
            return x & (-x)
        def add(x):
            while x<=Max:
                seg[x]+=1
                x+=low_bit(x)
        def query(x):
            x=min(x,Max)
            ret=0
            while x:
                ret+=seg[x]
                x-=low_bit(x)
            return ret
        
        ret=0
        N=len(arr)
        for j,xj in enumerate(arr):
            for k in range(j+1,N):
                xk=arr[k]
                if abs(xk-xj)>b:
                    continue
                l1,r1=xj-a,xj+a
                l2,r2=xk-c,xk+c
                l=max(0,l1,l2)
                r=min(r1,r2)
                if l>r:
                    continue
                ret+=query(r+1)-query(l)
            add(xj+1)
        return ret


# @lc code=end
assert Solution().countGoodTriplets(arr=[3, 0, 1, 1, 9, 7], a=7, b=2, c=3) == 4
assert Solution().countGoodTriplets([4,9,9,8,9,5,3,7],1,3,0) == 3
