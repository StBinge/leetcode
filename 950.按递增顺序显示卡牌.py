#
# @lc app=leetcode.cn id=950 lang=python3
#
# [950] 按递增顺序显示卡牌
#
from sbw import *
# @lc code=start
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        L=len(deck)
        ret=[-1]*L
        queue=deque(list(range(L)))
        # temp=deque()
        for i in deck:
            ret[queue.popleft()]=i
            if not queue:
                break
            queue.append(queue.popleft())
        return ret
# @lc code=end
deck=[17,13,11,2,3,5,7]
ret=[2,13,3,11,5,17,7]
assert Solution().deckRevealedIncreasing(deck)==ret
