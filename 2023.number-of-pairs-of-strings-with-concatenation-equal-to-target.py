#
# @lc app=leetcode.cn id=2023 lang=python3
# @lcpr version=30204
#
# [2023] 连接后等于目标字符串的字符串对
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        cnt = Counter(nums)
        ret = 0
        for i in range(1, len(target)):
            pre, suf = target[:i], target[i:]
            if pre != suf:
                ret += cnt[pre] * cnt[suf]
            else:
                ret += cnt[pre] * (cnt[pre] - 1)
        return ret


# @lc code=end
assert Solution().numOfPairs(nums=["1", "1", "1"], target="11") == 6
assert Solution().numOfPairs(["1201954", "543", "3", "12019"], "12019543") == 2
assert Solution().numOfPairs(nums=["123", "4", "12", "34"], target="1234") == 2
assert Solution().numOfPairs(nums=["777", "7", "77", "77"], target="7777") == 4


#
# @lcpr case=start
# ["777","7","77","77"]\n"7777"\n
# @lcpr case=end

# @lcpr case=start
# ["123","4","12","34"]\n"1234"\n
# @lcpr case=end

# @lcpr case=start
# ["1","1","1"]\n"11"\n
# @lcpr case=end

#
