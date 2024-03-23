#
# @lc app=leetcode.cn id=3048 lang=python3
#
# [3048] 标记所有下标的最早秒数 I
#
from sbw import *
# @lc code=start
class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        M=len(changeIndices)
        N=len(nums)
        tot=sum(nums)+len(nums)
        if tot>M:
            return -1

        marked=[0]*N
        def check(mx:int):
            mark=N
            need=0
            for i in range(mx-1,-1,-1):
                idx=changeIndices[i]-1
                if marked[idx]!=mx:
                    marked[idx]=mx
                    mark-=1
                    need+=nums[idx]
                elif need:
                    need-=1
            
            return mark==0 and need==0
        
        ret=tot+bisect_left(range(tot,M+1),True,key=check)
        return ret if ret<=M else -1

# @lc code=end
assert Solution().earliestSecondToMarkIndices([0,2,3,0],[2,4,1,3,3,3,3,3,3,2,1])==10
assert Solution().earliestSecondToMarkIndices([0,2],[2,1,2,2,1])==4
assert Solution().earliestSecondToMarkIndices([0],[1,1,1])==1
assert Solution().earliestSecondToMarkIndices(nums = [1,3], changeIndices = [1,1,1,2,1,1,1])==6
assert Solution().earliestSecondToMarkIndices(nums = [0,1], changeIndices = [2,2,2])==-1
assert Solution().earliestSecondToMarkIndices(nums = [2,2,0], changeIndices = [2,2,2,2,3,2,2,1])==8
