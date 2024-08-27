#
# @lc app=leetcode.cn id=1909 lang=python3
# @lcpr version=30204
#
# [1909] 删除一个元素使数组严格递增
#

from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        last1 = last2 = 0
        removed = False
        for n in nums:
            if n > last1:
                last1, last2 = n, last1
            else:
                if removed:
                    return False
                removed = True
                if n > last2:
                    last1 = n
        return True


# @lc code=end
assert Solution().canBeIncreasing([1, 2, 3,1,4,5])
assert Solution().canBeIncreasing([1, 2, 3])
assert not Solution().canBeIncreasing([1, 1, 1])
assert Solution().canBeIncreasing([1, 2, 10, 5, 7])
assert Solution().canBeIncreasing([2, 3, 1, 2]) == False


#
# @lcpr case=start
# [1,2,10,5,7]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#
