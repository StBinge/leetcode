#
# @lc app=leetcode.cn id=3041 lang=python3
#
# [3041] 修改数组后最大化数组中的连续元素数目
#
from sbw import *
# @lc code=start
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        f=defaultdict(int)
        for n in nums:
            f[n+1]=f[n]+1
            f[n]=f[n-1]+1
        return max(f.values())
            

            


# @lc code=end
assert Solution().maxSelectedElements([8,10,6,12,9,12,2,3,13,19,11,18,10,16])==8
assert Solution().maxSelectedElements([12])==1
assert Solution().maxSelectedElements([12,11,8,7,2,10,18,12])==6
assert Solution().maxSelectedElements([1,4,7,10])==1
assert Solution().maxSelectedElements(nums = [2,1,5,1,1])==3
