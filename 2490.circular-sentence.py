#
# @lc app=leetcode.cn id=2490 lang=python3
# @lcpr version=30204
#
# [2490] 回环句
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0]!=sentence[-1]:
            return False
        for i,ch in enumerate(sentence):
            if ch==' ' and sentence[i-1]!=sentence[i+1]:
                return False
        return True

# @lc code=end



#
# @lcpr case=start
# "leetcode exercises sound delightful"\n
# @lcpr case=end

# @lcpr case=start
# "eetcode"\n
# @lcpr case=end

# @lcpr case=start
# "Leetcode is cool"\n
# @lcpr case=end

#

