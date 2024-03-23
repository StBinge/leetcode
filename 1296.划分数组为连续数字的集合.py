#
# @lc app=leetcode.cn id=1296 lang=python3
#
# [1296] 划分数组为连续数字的集合
#
from sbw import *
# @lc code=start
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k:
            return False
        counter=Counter(nums)
        for key in sorted(counter.keys()):
            if counter[key]==0:
                continue
            v=counter[key]
            for i in range(k):
                if counter[key+i]<v:
                    return False
                counter[key+i]-=v
        return True
# @lc code=end
assert Solution().isPossibleDivide(nums = [1,2,3,4], k = 3)==False
assert Solution().isPossibleDivide(nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3)
assert Solution().isPossibleDivide(nums = [1,2,3,3,4,4,5,6], k = 4)
