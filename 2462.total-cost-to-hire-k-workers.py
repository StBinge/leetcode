#
# @lc app=leetcode.cn id=2462 lang=python3
# @lcpr version=30204
#
# [2462] 雇佣 K 位工人的总代价
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        N = len(costs)
        if candidates * 2 + k > N:
            return sum(heapq.nsmallest(k, costs))
        left_heap=costs[:candidates]
        right_heap=costs[N-candidates:]
        heapq.heapify(left_heap)
        heapq.heapify(right_heap)
        ret=0
        left=candidates
        right=N-candidates-1
        for _ in range(k):
            if left_heap[0]<=right_heap[0]:
                ret+=heapq.heapreplace(left_heap,costs[left])
                left+=1
            else:
                ret+=heapq.heapreplace(right_heap,costs[right])
                right-=1
        return ret


# @lc code=end
assert (
    Solution().totalCost(
        [
            69,
            10,
            63,
            24,
            1,
            71,
            55,
            46,
            4,
            61,
            78,
            21,
            85,
            52,
            83,
            77,
            42,
            21,
            73,
            2,
            80,
            99,
            98,
            89,
            55,
            94,
            63,
            50,
            43,
            62,
            14,
        ],
        21,
        31,
    )
    == 829
)
assert (
    Solution().totalCost(
        [31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58], 11, 2
    )
    == 423
)
assert Solution().totalCost(costs=[1, 2, 4, 1], k=3, candidates=3) == 4
assert Solution().totalCost([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4) == 11


#
# @lcpr case=start
# [17,12,10,2,7,2,11,20,8]\n3\n4\n
# @lcpr case=end

# @lcpr case=start
# [1,2,4,1]\n3\n3\n
# @lcpr case=end

#
