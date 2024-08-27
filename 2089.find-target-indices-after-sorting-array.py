#
# @lc app=leetcode.cn id=2089 lang=python3
# @lcpr version=30204
#
# [2089] 找出数组排序后的目标下标
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        small=0
        same=0
        for n in nums:
            small+=n<target
            same+=n==target
        return [i for i in range(small,small+same)]
# @lc code=end



#
# @lcpr case=start
# [1,2,5,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,5,2,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,5,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,2,5,2,3]\n4\n
# @lcpr case=end

#

