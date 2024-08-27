#
# @lc app=leetcode.cn id=1733 lang=python3
#
# [1733] 需要教语言的最少人数
#
from sbw import *


# @lc code=start
class Solution:
    def minimumTeachings(
        self, n: int, languages: List[List[int]], friendships: List[List[int]]
    ) -> int:
        M = len(languages)
        friends = [[] for _ in range(M + 1)]
        people_of_lang = [set() for _ in range(n + 1)]
        for p, lans in enumerate(languages):
            for lan in lans:
                people_of_lang[lan].add(p)

        def can_talk(x, y):
            for lan in languages[x]:
                if y in people_of_lang[lan]:
                    return True
            return False

        can_not_talks=set()
        lang_cnt=[0]*(n+1)
        for x, y in friendships:
            x -= 1
            y -= 1
            if can_talk(x, y):
                continue
            can_not_talks.add(x)
            can_not_talks.add(y)
        for p in can_not_talks:
            for lan in languages[p]:
                lang_cnt[lan]+=1

        return len(can_not_talks)-max(lang_cnt)


# @lc code=end
assert Solution().minimumTeachings(n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]])==2
assert (
    Solution().minimumTeachings(
        n=2, languages=[[1], [2], [1, 2]], friendships=[[1, 2], [1, 3], [2, 3]]
    )
    == 1
)
