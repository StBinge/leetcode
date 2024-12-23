#
# @lc app=leetcode.cn id=LCR 181 lang=python3
# @lcpr version=30204
#
# [LCR 181] 字符串中的单词反转
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def reverseMessage(self, message: str) -> str:
        words=message.split(' ')
        return ' '.join([word for word in words[::-1] if word])

# @lc code=end
assert Solution().reverseMessage(" hello world!  ")=="world! hello"


#
# @lcpr case=start
# "the sky is blue"\n
# @lcpr case=end

# @lcpr case=start
# "  hello world!  "\n
# @lcpr case=end

# @lcpr case=start
# "a good   example"\n
# @lcpr case=end

#

