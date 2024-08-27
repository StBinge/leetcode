#
# @lc app=leetcode.cn id=1544 lang=python3
#
# [1544] 整理字符串
#


# @lc code=start
class Solution:
    def makeGood(self, s: str) -> str:
        ret = []
        for ch in s:
            if ret and ord(ret[-1]) ^ ord(ch)== 32:
                ret.pop()
                continue
            else:
                ret.append(ch)
        return "".join(ret)


# @lc code=end
assert Solution().makeGood("s") == "s"
assert Solution().makeGood("abBAcC") == ""
assert Solution().makeGood("leEeetcode") == "leetcode"
