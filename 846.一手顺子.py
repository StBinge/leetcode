#
# @lc app=leetcode.cn id=846 lang=python3
#
# [846] 一手顺子
#
from typing import List
# @lc code=start
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize:
            return False
        counter = Counter(hand)
        sorted_keys = sorted(counter.keys())
        for key in sorted_keys:
            if counter[key] > 0:
                v = counter[key]
                for i in range(groupSize):
                    cnt = counter.get(key+i, 0)-v
                    if cnt < 0:
                        return False
                    counter[key+i] = cnt
        return True
# @lc code=end


hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3
assert Solution().isNStraightHand(hand, groupSize)
hand = [1, 2, 3, 4, 5]
groupSize = 4
assert Solution().isNStraightHand(hand, groupSize) == False
