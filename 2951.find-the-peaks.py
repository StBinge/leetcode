#
# @lc app=leetcode.cn id=2951 lang=python3
# @lcpr version=30204
#
# [2951] 找出峰值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        return [i for i in range(1,len(mountain)-1) if mountain[i-1]<mountain[i]>mountain[i+1]]
# @lc code=end



#
# @lcpr case=start
# [2,4,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,4,3,8,5]\n
# @lcpr case=end

#

