#
# @lc app=leetcode.cn id=2825 lang=python3
# @lcpr version=30204
#
# [2825] 循环增长使字符串子序列等于另一个字符串
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        N = len(str1)
        if N<len(str2):
            return False
        idx = 0
        for ch in str2:
            while idx < N and (ord(ch)-ord(str1[idx]))%26>1:
                idx += 1
            if idx == N:
                return False
            idx+=1
        return True


# @lc code=end
assert Solution().canMakeSubsequence("abc", "abcd")==False
assert Solution().canMakeSubsequence("zc", "ad")
assert Solution().canMakeSubsequence("abc", "ad")

#
# @lcpr case=start
# "abc"\n"ad"\n
# @lcpr case=end

# @lcpr case=start
# "zc"\n"ad"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n"d"\n
# @lcpr case=end

#
