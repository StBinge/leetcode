#
# @lc app=leetcode.cn id=2315 lang=python3
# @lcpr version=30204
#
# [2315] 统计星号
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countAsterisks(self, s: str) -> int:
        ret=0
        between=False
        for ch in s:
            if ch=='|':
                between=not between
            elif ch=='*':
                ret+=not between
        return ret
        
# @lc code=end



#
# @lcpr case=start
# "l|*e*et|c**o|*de|"\n
# @lcpr case=end

# @lcpr case=start
# "iamprogrammer"\n
# @lcpr case=end

# @lcpr case=start
# "yo|uar|e**|b|e***au|tifu|l"\n
# @lcpr case=end

#

