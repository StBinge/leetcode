#
# @lc app=leetcode.cn id=2042 lang=python3
# @lcpr version=30204
#
# [2042] 检查句子中的数字是否递增
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        pre=0
        num=0

        for ch in s:
            if ch==' ':
                if num==0:
                    continue
                else:
                    if num<=pre:
                        return False
                    pre=num
                    num=0
            elif ch.isnumeric():
                num=num*10+int(ch)

        return num==0 or num>pre


# @lc code=end
assert Solution().areNumbersAscending("hello world 5 x 5")==False
assert Solution().areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles")


#
# @lcpr case=start
# "1 box has 3 blue 4 red 6 green and 12 yellow marbles"\n
# @lcpr case=end

# @lcpr case=start
# "hello world 5 x 5"\n
# @lcpr case=end

# @lcpr case=start
# "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"\n
# @lcpr case=end

# @lcpr case=start
# "4 5 11 26"\n
# @lcpr case=end

#

