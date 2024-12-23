#
# @lc app=leetcode.cn id=3340 lang=python3
# @lcpr version=30204
#
# [3340] 检查平衡字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isBalanced(self, num: str) -> bool:
        return sum(int(num[i]) for i in range(0,len(num),2))==sum(int(num[i]) for i in range(1,len(num),2))
# @lc code=end



#
# @lcpr case=start
# "1234"\n
# @lcpr case=end

# @lcpr case=start
# "24123"\n
# @lcpr case=end

#

