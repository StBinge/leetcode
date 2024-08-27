#
# @lc app=leetcode.cn id=1903 lang=python3
# @lcpr version=30204
#
# [1903] 字符串中的最大奇数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if int(num[i])&1:
                return num[:i+1]
        return ''
# @lc code=end



#
# @lcpr case=start
# "52"\n
# @lcpr case=end

# @lcpr case=start
# "4206"\n
# @lcpr case=end

# @lcpr case=start
# "35427"\n
# @lcpr case=end

#

