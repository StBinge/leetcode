#
# @lc app=leetcode.cn id=3080 lang=python3
#
# [3080] 执行操作标记数组中的元素
#
from sbw import *
# @lc code=start

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s=sum(nums)
        L=len(nums)
        sorted_idx=sorted(range(L),key=nums.__getitem__)
  

        ret=[0]*len(queries)
        point=0
        for i in range(len(queries)):
            idx,k=queries[i]
            s-=nums[idx]
            nums[idx]=0
            while k and point<L:
                if k>=L-point:
                    return ret
                _idx=sorted_idx[point]
                if nums[_idx]==0:
                    point+=1
                    continue
                s-=nums[_idx]
                nums[_idx]=0
                k-=1
                point+=1
            ret[i]=s
        return ret
            
# @lc code=end

assert Solution().unmarkedSumArray(nums = [1,4,2,3], queries = [[0,1]])==[7]
assert Solution().unmarkedSumArray(nums = [1,2,2,1,2,3,1], queries = [[1,2],[3,3],[4,2]])==[8,3,0]