#
# @lc app=leetcode.cn id=2517 lang=python3
# @lcpr version=30204
#
# [2517] 礼盒的最大甜蜜度
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price = set(price)
        if len(price) < k:
            return 0
        price = sorted(price)
        left = 0
        right = (price[-1] - price[0])//(k-1)
        ret = 0

        def check(x):
            pre=price[0]
            cnt=1
            for p in price:
                if p>=pre+x:
                    cnt+=1
                    pre=p
            return cnt>=k

        while left <= right:
            mid = (left + right) >> 1
            if check(mid):
                ret = mid
                left = mid + 1
            else:
                right = mid - 1
        return ret


# @lc code=end
assert Solution().maximumTastiness(price=[7, 7, 7, 7], k=2) == 0
assert Solution().maximumTastiness(price=[1, 3, 1], k=2) == 2
assert Solution().maximumTastiness(price=[13, 5, 1, 8, 21, 2], k=3) == 8


#
# @lcpr case=start
# [13,5,1,8,21,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,3,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7]\n2\n
# @lcpr case=end

#
