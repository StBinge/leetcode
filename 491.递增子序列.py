#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#
from typing import List
# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
 
        ret=[]
        def dfs(idx,last,temp:list):
            if idx==len(nums):
                if len(temp)>1:
                    ret.append(temp.copy())
                return 
            if nums[idx]>=last:
                temp.append(nums[idx])
                dfs(idx+1,nums[idx],temp)
                temp.pop()
            
            if nums[idx]!=last:
                dfs(idx+1,last,temp)

        dfs(0,-200,[])
        return ret


# @lc code=end
# ret=Solution().findSubsequences([4,6,7,7])
# print(ret)
# assert len(ret)==8


ret=Solution().findSubsequences([4,6,7,7])
print(ret)
assert len(ret)==8
ret= Solution().findSubsequences([4,4,3,2,1])
print(ret)
assert len(ret)==1