#
# @lc app=leetcode.cn id=2546 lang=python3
# @lcpr version=30204
#
# [2546] 执行逐位运算使字符串相等
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        return ('1' in s) == ('1' in target)
# @lc code=end
assert not Solution().makeStringsEqual(s = "11", target = "00")
assert Solution().makeStringsEqual('1010','0110')


#
# @lcpr case=start
# "1010"\n"0110"\n
# @lcpr case=end

# @lcpr case=start
# "11"\n"00"\n
# @lcpr case=end

#

