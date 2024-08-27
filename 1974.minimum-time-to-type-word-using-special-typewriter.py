#
# @lc app=leetcode.cn id=1974 lang=python3
# @lcpr version=30204
#
# [1974] 使用特殊打字机键入单词的最少时间
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minTimeToType(self, word: str) -> int:
        ret=0
        cur=ord('a')
        for ch in word:
            code=ord(ch)
            move=min(abs(cur-code),cur+26-code,code+26-cur)
            ret+=move+1
            cur=code
        return ret
# @lc code=end
assert Solution().minTimeToType('zjpc')==34
assert Solution().minTimeToType('bza')==7
assert Solution().minTimeToType('abc')==5


#
# @lcpr case=start
# "abc"\n
# @lcpr case=end

# @lcpr case=start
# "bza"\n
# @lcpr case=end

# @lcpr case=start
# "zjpc"\n
# @lcpr case=end

#

