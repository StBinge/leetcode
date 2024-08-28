#
# @lc app=leetcode.cn id=1945 lang=python3
# @lcpr version=30204
#
# [1945] 字符串转化后的各位数字之和
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        sum = 0
        for ch in s:
            code = ord(ch) - ord("a") + 1
            sum += code % 10 + code // 10
        for _ in range(k-1):
            ss = 0
            while sum:
                ss += sum % 10
                sum //= 10
            sum = ss
        return sum


# @lc code=end
assert Solution().getLucky(s = "iiii", k = 1) == 36
assert Solution().getLucky("leetcode", 2) == 6


#
# @lcpr case=start
# "iiii"\n1\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n2\n
# @lcpr case=end

#
