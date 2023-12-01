#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#
from typing import List
# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N=len(nums)
        id_map={}
        idx=1
        for n in sorted(nums):
            if n not in id_map:
                id_map[n]=idx
                idx+=1

        tri=[[0,0] for _ in range(2001)]
        def low_bit(x:int):
            return x&-x
    
        def add(x,info:list):
            while x<=N:
                length,cnt=tri[x]
                if length==info[0]:
                    cnt+=info[1]
                elif length<info[0]:
                    cnt=info[1]
                    length=info[0]
                tri[x]=[length,cnt]
                x+=low_bit(x)

        def query(x):
            length,cnt=0,0
            while x>0:
                if tri[x][0]>length:
                    cnt=tri[x][1]
                    length=tri[x][0]
                elif tri[x][0]==length:
                    cnt+=tri[x][1]
                x-=low_bit(x)
            return length,cnt
        
        for n in nums:
            x=id_map[n]
            info=query(x-1)
            add(x,[info[0]+1,max(info[1],1)])
        
        return query(N)[1]
# @lc code=end
assert Solution().findNumberOfLIS([1,2,4,3,5,4,7,2])==3
assert Solution().findNumberOfLIS([2,2,2,2,2])==5
assert Solution().findNumberOfLIS([1,3,5,4,7])==2

