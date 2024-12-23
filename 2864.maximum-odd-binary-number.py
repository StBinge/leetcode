#
# @lc app=leetcode.cn id=2864 lang=python3
# @lcpr version=30204
#
# [2864] 最大二进制奇数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one=s.count('1')
        return ('1'*(one-1))+('0'*(len(s)-one))+'1'
    
# @lc code=end



#
# @lcpr case=start
# "010"\n
# @lcpr case=end

# @lcpr case=start
# "0101"\n
# @lcpr case=end

#

