#
# @lc app=leetcode.cn id=3011 lang=python3
# @lcpr version=30204
#
# [3011] 判断一个数组是否可以变为有序
#
from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:

        pre_max=mx=0
        bits=0
        for n in nums:
            cnt = n.bit_count()
            if cnt == bits:
                mx=max(mx,n)
            else:
                pre_max=mx
                mx=n
                bits=cnt
            if n<pre_max:
                return False
        return True


# @lc code=end
assert not Solution().canSortArray([20,16])
assert not Solution().canSortArray([3,16,8,4,2])
assert Solution().canSortArray([1, 2, 3, 4, 5])
assert Solution().canSortArray([8, 4, 2, 30, 15])


#
# @lcpr case=start
# [8,4,2,30,15]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,16,8,4,2]\n
# @lcpr case=end

#
