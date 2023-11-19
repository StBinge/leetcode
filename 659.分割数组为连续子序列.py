#
# @lc app=leetcode.cn id=659 lang=python3
#
# [659] 分割数组为连续子序列
#
from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counter=Counter(nums)
        seg_counter=Counter()
        for n in nums:
            if counter[n]==0:
                continue
            if seg_counter[n-1]>0:
                seg_counter[n-1]-=1
                seg_counter[n]+=1
                counter[n]-=1
            else:
                if counter[n+1]<1 or counter[n+2]<1:
                    return False
                counter[n]-=1
                counter[n+1]-=1
                counter[n+2]-=1
                seg_counter[n+2]+=1
        
        return True
# @lc code=end

assert Solution().isPossible([1,2,3,3,4,5])
assert Solution().isPossible([1,2,3,4,4,5])==False
assert Solution().isPossible([1,2,3,3,4,4,5,5])
