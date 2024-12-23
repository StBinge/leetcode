#
# @lc app=leetcode.cn id=3280 lang=python3
# @lcpr version=30204
#
# [3280] 将日期转换为二进制表示
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return '-'.join(map(lambda x:bin(int(x))[2:],date.split('-')))
# @lc code=end



#
# @lcpr case=start
# "2080-02-29"\n
# @lcpr case=end

# @lcpr case=start
# "1900-01-01"\n
# @lcpr case=end

#

