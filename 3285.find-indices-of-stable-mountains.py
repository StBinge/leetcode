#
# @lc app=leetcode.cn id=3285 lang=python3
# @lcpr version=30204
#
# [3285] 找到稳定山的下标
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        return [i for i in range(1,len(height)) if height[i-1]>threshold]
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [10,1,10,1,10]\n3\n
# @lcpr case=end

# @lcpr case=start
# [10,1,10,1,10]\n10\n
# @lcpr case=end

#

