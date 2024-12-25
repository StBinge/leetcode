#
# @lc app=leetcode.cn id=3100 lang=python3
# @lcpr version=30204
#
# [3100] 换水问题 II
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ret=numBottles
        while numBottles>=numExchange:
            ret+=1
            numBottles-=numExchange-1
            numExchange+=1
        return ret


# @lc code=end

assert Solution().maxBottlesDrunk(10,3) == 13
assert Solution().maxBottlesDrunk(13, 6) == 15

#
# @lcpr case=start
# 13\n6\n
# @lcpr case=end

# @lcpr case=start
# 10\n3\n
# @lcpr case=end

#
