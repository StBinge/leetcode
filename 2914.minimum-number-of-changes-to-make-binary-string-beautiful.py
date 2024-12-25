#
# @lc app=leetcode.cn id=2914 lang=python3
# @lcpr version=30204
#
# [2914] 使二进制字符串变美丽的最少修改次数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minChanges(self, s: str) -> int:
        return sum(s[i]!=s[i+1] for i in range(0,len(s),2))
        
# @lc code=end



#
# @lcpr case=start
# "1001"\n
# @lcpr case=end

# @lcpr case=start
# "10"\n
# @lcpr case=end

# @lcpr case=start
# "0000"\n
# @lcpr case=end

#

