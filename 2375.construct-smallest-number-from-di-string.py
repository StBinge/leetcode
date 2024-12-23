#
# @lc app=leetcode.cn id=2375 lang=python3
# @lcpr version=30204
#
# [2375] 根据模式串构造最小数字
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = []
        for x in map(len, pattern.split('I')):
            ans.extend(range(len(ans) + x + 1 , len(ans), -1))
        return ''.join(map(str, ans))
# @lc code=end
assert Solution().smallestNumber('DDD')=='4321'
assert Solution().smallestNumber('IIIDIDDD')=='123549876'


#
# @lcpr case=start
# "IIIDIDDD"\n
# @lcpr case=end

# @lcpr case=start
# "DDD"\n
# @lcpr case=end

#

