#
# @lc app=leetcode.cn id=1922 lang=python3
# @lcpr version=30204
#
# [1922] 统计好数字的数目
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        Mod=10**9+7
        def quick_mul(x,y):
            ret,mul=1,x
            while y:
                if y&1:
                    ret=ret*mul%Mod
                mul=mul*mul%Mod
                y//=2
            return ret
        even = (n + 1) // 2
        odd = n - even
        return quick_mul(5,even)*quick_mul(4,odd)%Mod


# @lc code=end

assert Solution().countGoodNumbers(50) == 564908303
assert Solution().countGoodNumbers(4) == 400
assert Solution().countGoodNumbers(1) == 5

#
# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 50\n
# @lcpr case=end

#
