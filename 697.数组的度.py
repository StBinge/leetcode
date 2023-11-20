#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#
from typing import List
# @lc code=start
# from collections import Counter
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counter={}
        for i,n in enumerate(nums):
            if n in counter:
                counter[n][0]+=1
                counter[n][2]=i
            else:
                counter[n]=[1,i,i]
        minLen=len(nums)
        maxCnt=0
        for cnt,left,right in counter.values():
            if cnt>maxCnt:
                maxCnt=cnt
                minLen=right-left+1
            elif cnt==maxCnt:
                span=right-left+1
                if span<minLen:
                    minLen=span
        return minLen

# @lc code=end

assert Solution().findShortestSubArray([1,2,2,3,1])==2
assert Solution().findShortestSubArray([1,2,2,3,1,4,2])==6