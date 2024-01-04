#
# @lc app=leetcode.cn id=1103 lang=python3
#
# [1103] 分糖果 II
#
from sbw import *
# @lc code=start
import math
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        l,r=0,int(math.sqrt(candies*2))+1
        while l<r:
            mid=(l+r)>>1
            tot=(1+mid)*mid//2
            if tot<candies:
                l=mid+1
            else:
                r=mid
        
        remain=candies-(r+1)*r//2

        loop=r//num_people
        ret=[0]*num_people
        if loop:
            ret[0]=(2+(loop-1)*num_people)*loop//2
            for i in range(1,num_people):
                ret[i]=ret[i-1]+loop
        cnt=1+loop*num_people
        for i in range(r%num_people):
            ret[i]+=cnt
            cnt+=1
        if remain<0:
            ret[r%num_people-1]+=remain
        return ret
# @lc code=end
assert Solution().distributeCandies(candies = 60, num_people = 4)==[15,18,15,12]
assert Solution().distributeCandies(candies = 90, num_people = 4)==[27,18,21,24]
assert Solution().distributeCandies(candies = 1, num_people = 3)==[1,0,0]
assert Solution().distributeCandies(candies = 10, num_people = 3)==[5,2,3]
assert Solution().distributeCandies(candies = 7, num_people = 4)==[1,2,3,1]
