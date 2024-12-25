#
# @lc app=leetcode.cn id=2578 lang=python3
# @lcpr version=30204
#
# [2578] 最小和分割
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def splitNum(self, num: int) -> int:
        s=sorted(str(num))
        return int(''.join(s[::2]))+int(''.join(s[1::2]))

        

# @lc code=end



#
# @lcpr case=start
# 4325\n
# @lcpr case=end

# @lcpr case=start
# 687\n
# @lcpr case=end

#

