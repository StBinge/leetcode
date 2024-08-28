#
# @lc app=leetcode.cn id=2117 lang=python3
# @lcpr version=30204
#
# [2117] 一个区间内所有数乘积的缩写
#
from sbw import *


def count10(left, right):
    cnt2 = cnt5 = 0
    for i in range(left, right + 1):
        while i % 2 == 0:
            i //= 2
            cnt2 += 1
        while i % 5 == 0:
            i //= 5
            cnt5 += 1
    return min(cnt2, cnt5)


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        suf = 1
        c = 0
        limit = 10**20
        pre = 1
        cnt2 = cnt5 = 0
        suf_limit=10**10
   
        for i in range(left, right + 1):
            while i % 2 == 0:
                i //= 2
                cnt2 += 1
            while i % 5 == 0:
                i //= 5
                cnt5 += 1
            pre *= i
            while pre > limit:
                pre //= 10

            suf *= i
            suf%=suf_limit

        c = min(cnt2, cnt5)

        cnt2 -= c
        cnt5 -= c

        base = 2
        exp = cnt2
        if cnt5:
            base = 5
            exp = cnt5

        for i in range(exp):
            pre*=base
            while pre>limit:
                pre//=10

        suf = (suf * (pow(base, exp, suf_limit))) % suf_limit

        if pre>=10**10:
            while pre >= 10**5:
                pre //= 10
            suf %= 10**5
            return str(pre) + "..." + str(suf).rjust(5, "0") + "e" + str(c)
        return str(suf) + "e" + str(c)


# @lc code=end
# left = 4838
# right = 6168
# assert Solution().abbreviateProduct(left, right) == count10(left, right)
ret = Solution().abbreviateProduct(4649,4651)
assert ret == "10054...62035e1"
ret = Solution().abbreviateProduct(4838,6186)
assert ret == "36088...36896e337"
ret = Solution().abbreviateProduct(3543, 4907)
assert ret == "45166...62976e341"
ret = Solution().abbreviateProduct(4838, 6168)
assert ret == "21024...92672e332"
ret = Solution().abbreviateProduct(7298, 7327)
assert ret == "83554...37504e8"
ret = Solution().abbreviateProduct(2763, 3870)
assert ret == "45352...52736e277"
ret = Solution().abbreviateProduct(3787, 5136)
assert ret == "35233...72992e337"
ret = Solution().abbreviateProduct(44, 9556)
assert ret == "10205...06688e2378"
ret = Solution().abbreviateProduct(371, 375)
assert ret == "7219856259e3"
assert Solution().abbreviateProduct(2, 11) == "399168e2"
assert Solution().abbreviateProduct(1, 4) == "24e0"


#
# @lcpr case=start
# 1\n4\n
# @lcpr case=end

# @lcpr case=start
# 2\n11\n
# @lcpr case=end

# @lcpr case=start
# 371\n375\n
# @lcpr case=end

#
