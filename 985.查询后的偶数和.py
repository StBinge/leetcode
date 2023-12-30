#
# @lc app=leetcode.cn id=985 lang=python3
#
# [985] 查询后的偶数和
#
from sbw import *
# @lc code=start
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s=sum(x for x in nums if x%2==0)
        ret=[]
        for val,idx in queries:
            if nums[idx]%2==0:
                s-=nums[idx]
            nums[idx]+=val
            if nums[idx]%2==0:
                s+=nums[idx]

            ret.append(s)
        return ret
# @lc code=end
A = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
ret=[8,6,2,4]
assert Solution().sumEvenAfterQueries(A,queries)==ret