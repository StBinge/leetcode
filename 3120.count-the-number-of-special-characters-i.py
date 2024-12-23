#
# @lc app=leetcode.cn id=3120 lang=python3
# @lcpr version=30204
#
# [3120] 统计特殊字母的数量 I
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        mask1=mask2=0
        for ch in word:
            if ch.isupper():
                mask1|=1<<(ord(ch)-ord('A'))
            else:
                mask2|=1<<(ord(ch)-ord('a'))
        return (mask1&mask2).bit_count()

# @lc code=end



#
# @lcpr case=start
# "aaAbcBC"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n
# @lcpr case=end

# @lcpr case=start
# "abBCab"\n
# @lcpr case=end

#

