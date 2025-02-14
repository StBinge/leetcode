#
# @lc app=leetcode.cn id=2572 lang=python3
# @lcpr version=30204
#
# [2572] 无平方子集计数
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        cnt=[0]*31
        for n in nums:
            cnt[n]+=1
        invaids=[4,8,9,12,16,18,20,24,25,28]
        ret=1
        for i in range(1,31):
            if i in invaids:
                continue
            
# @lc code=end



#
# @lcpr case=start
# [3,4,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

