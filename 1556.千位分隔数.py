#
# @lc app=leetcode.cn id=1556 lang=python3
#
# [1556] 千位分隔数
#


# @lc code=start
class Solution:
    def thousandSeparator(self, n: int) -> str:
        ret = []

        while True:
            d = n % 1000
            n //= 1000
            if n:
                ret.append(str(d).rjust(3,"0"))
                ret.append(".")
            else:
                ret.append(str(d))
                break

        return "".join(ret[::-1])


# @lc code=end
assert Solution().thousandSeparator(51040) == "51.040"
assert Solution().thousandSeparator(0) == "0"
assert Solution().thousandSeparator(1234) == "1.234"
assert Solution().thousandSeparator(987)=='987'
