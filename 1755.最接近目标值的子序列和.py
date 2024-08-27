#
# @lc app=leetcode.cn id=1755 lang=python3
#
# [1755] 最接近目标值的子序列和
#
from sbw import *

# @lc code=start
from sortedcontainers import SortedSet


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        N=len(nums)
        def make(ar:list):
            ret=set([0])
            temp=set()
            for n in ar:
                for pre in ret:
                    temp.add(pre+n)
                ret.update(temp)
            return sorted(ret)
        
        s1=make(nums[:N//2])
        s2=make(nums[N//2:])
        ret=float('inf')
        l1=len(s1)
        i1=0
        i2=len(s2)-1
        while i1<l1 and i2>=0:
            s=s1[i1]+s2[i2]
            ret=min(ret,abs(s-goal))
            if s>goal:
                i2-=1
            elif s<goal:
                i1+=1
            else:
                return 0
        return ret



# @lc code=end
assert Solution().minAbsDifference([-7933,-1642,-6137,6234,4728,5474,2439],-428059487) == 428043775
assert Solution().minAbsDifference(nums=[1, 2, 3], goal=-7) == 7
assert Solution().minAbsDifference(nums=[7, -9, 15, -2], goal=-5) == 1
assert Solution().minAbsDifference(nums=[5, -7, 3, 5], goal=6) == 0
