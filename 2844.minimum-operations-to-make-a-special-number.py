#
# @lc app=leetcode.cn id=2844 lang=python3
# @lcpr version=30204
#
# [2844] 生成特殊数字的最少操作
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumOperations(self, num: str) -> int:
        N = len(num)
        ret = N
        idx = N - 1
        while idx >= 0 and num[idx] != "0":
            idx -= 1
        if idx>=0:
            ret=N-1
        idx -= 1
        while idx >= 0 and num[idx] not in "05":
            idx -= 1
        if idx >= 0:
            ret = min(ret, N - idx - 2)


        idx = N - 1
        while idx >= 0 and num[idx] != "5":
            idx -= 1
        idx -= 1
        while idx >= 0 and num[idx] not in "27":
            idx -= 1
        if idx >= 0:
            ret = min(ret, N - idx - 2)
        return ret


# @lc code=end
assert Solution().minimumOperations("10") == 1
assert Solution().minimumOperations("2908305") == 3
assert Solution().minimumOperations("2245047") == 2


#
# @lcpr case=start
# "2245047"\n
# @lcpr case=end

# @lcpr case=start
# "2908305"\n
# @lcpr case=end

# @lcpr case=start
# "10"\n
# @lcpr case=end

#
