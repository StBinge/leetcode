#
# @lc app=leetcode.cn id=LCP 40 lang=python3
# @lcpr version=30204
#
# [LCP 40] 心算挑战
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort(reverse=True)
        s=sum(cards[:cnt])
        if s&1==0:
            return s

        ret=0
        x=cards[cnt-1]
        for n in cards[cnt:]:
            if n&1 != x&1:
                ret=s+n-x
                break
        for n in cards[cnt-1::-1]:
            if n&1 != x&1:
                for nn in cards[cnt:]:
                    if n&1 !=nn&1:
                        ret=max(ret,s-n+nn)
                        return ret
        return ret

# @lc code=end
assert Solution().maxmiumScore([9,7,1,4,9],1) == 4
assert Solution().maxmiumScore([9,5,9,1,6,10,3,4,5,1],2) == 18
assert Solution().maxmiumScore([1,3,4,5],4) == 0
assert Solution().maxmiumScore([3,1,6,9,2,4,9,2,3],4) == 28
assert Solution().maxmiumScore([1,10,5,2,9],4) == 26
assert Solution().maxmiumScore(cards=[3, 3, 1], cnt=1) == 0
assert Solution().maxmiumScore([7, 5], 2) == 12
assert Solution().maxmiumScore(cards=[1, 2, 8, 9], cnt=3) == 18


#
# @lcpr case=start
# [1,2,8,9]\n3`>\n
# @lcpr case=end

# @lcpr case=start
# [3,3,1]\n1`>\n
# @lcpr case=end

#
