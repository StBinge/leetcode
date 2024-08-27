#
# @lc app=leetcode.cn id=2000 lang=python3
# @lcpr version=30204
#
# [2000] 反转单词前缀
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i,c in enumerate(word):
            if c==ch:
                return word[i::-1]+word[i+1:]
        return word
# @lc code=end



#
# @lcpr case=start
# "abcdefd"\n"d"\n
# @lcpr case=end

# @lcpr case=start
# "xyxzxe"\n"z"\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n"z"\n
# @lcpr case=end

#

