#
# @lc app=leetcode.cn id=2486 lang=python3
# @lcpr version=30204
#
# [2486] 追加字符以获得子序列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        M=len(t)
        tid=0
        for ch in s:
            if ch==t[tid]:
                tid+=1
                if tid==M:
                    break
        return M-tid
# @lc code=end



#
# @lcpr case=start
# "coaching"\n"coding"\n
# @lcpr case=end

# @lcpr case=start
# "abcde"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "z"\n"abcde"\n
# @lcpr case=end

#

