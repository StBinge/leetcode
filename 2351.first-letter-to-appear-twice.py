#
# @lc app=leetcode.cn id=2351 lang=python3
# @lcpr version=30204
#
# [2351] 第一个出现两次的字母
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen=set()
        for ch in s:
            if ch in seen:
                return ch
            seen.add(ch)
        
# @lc code=end



#
# @lcpr case=start
# "abccbaacz"\n
# @lcpr case=end

# @lcpr case=start
# "abcdd"\n
# @lcpr case=end

#

