#
# @lc app=leetcode.cn id=2259 lang=python3
# @lcpr version=30204
#
# [2259] 移除指定数字得到的最大结果
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        last = -1
        for i, ch in enumerate(number):
            if ch == digit:
                last = i
                if i + 1 < len(number) and number[i + 1] > digit:
                    break

        return number[:last] + number[last + 1 :]


# @lc code=end
assert Solution().removeDigit("551", "5") == "51"
assert Solution().removeDigit("73197", "7") == "7319"
assert Solution().removeDigit("58577", "5") == "8577"
assert Solution().removeDigit("1231", "1") == "231"
assert Solution().removeDigit("123", "3") == "12"


#
# @lcpr case=start
# "123"\n"3"\n
# @lcpr case=end

# @lcpr case=start
# "1231"\n"1"\n
# @lcpr case=end

# @lcpr case=start
# "551"\n"5"\n
# @lcpr case=end

#
