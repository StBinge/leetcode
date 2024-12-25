#
# @lc app=leetcode.cn id=3121 lang=python3
# @lcpr version=30204
#
# [3121] 统计特殊字母的数量 II
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        invalid = 0
        upper = 0
        lower = 0
        for ch in word:
            code=ord(ch)
            bit=1<<(code&31)
            if code&32:
                lower|=bit
                if upper&bit:
                    invalid|=bit
            else:
                upper|=bit
        return (upper&lower^invalid).bit_count()

# @lc code=end
assert Solution().numberOfSpecialChars("aaAbcBC") == 3
assert Solution().numberOfSpecialChars("abc") == 0


#
# @lcpr case=start
# "aaAbcBC"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n
# @lcpr case=end

# @lcpr case=start
# "AbBCab"\n
# @lcpr case=end

#
