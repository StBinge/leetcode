#
# @lc app=leetcode.cn id=2092 lang=python3
# @lcpr version=30204
#
# [2092] 找出知晓秘密的所有专家
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        # knonw = set([0, firstPerson])
        know=[False]*n
        know[0]=know[firstPerson]=True

        meetings.sort(key=lambda x: x[2])
        N = len(meetings)
        idx = 0
        while idx < N:
            j = idx + 1
            while j < N and meetings[j][2] == meetings[idx][2]:
                j += 1
            adj = defaultdict(list)
            points=set()
            for k in range(idx, j):
                x, y, _ = meetings[k]
                adj[x].append(y)
                adj[y].append(x)
                points.add(x)
                points.add(y)

            q = [i for i in points if know[i]]
            while q:
                cur = q.pop()
                for nei in adj[cur]:
                    if not know[nei]:
                        know[nei]=True
                        q.append(nei)
            idx = j

        return [i for i in range(n) if know[i]]


# @lc code=end
assert sorted(Solution().findAllPeople(5, [[1, 4, 3], [0, 4, 3]], 3)) == [0, 1, 3, 4]
assert sorted(
    Solution().findAllPeople(
        n=4, meetings=[[3, 1, 3], [1, 2, 2], [0, 3, 3]], firstPerson=3
    )
) == [0, 1, 3]
assert sorted(Solution().findAllPeople(6, [[0, 2, 1], [1, 3, 1], [4, 5, 1]], 1)) == [
    0,
    1,
    2,
    3,
]
assert sorted(
    Solution().findAllPeople(
        n=5, meetings=[[3, 4, 2], [1, 2, 1], [2, 3, 1]], firstPerson=1
    )
) == [0, 1, 2, 3, 4]
assert sorted(
    Solution().findAllPeople(
        n=6, meetings=[[1, 2, 5], [2, 3, 8], [1, 5, 10]], firstPerson=1
    )
) == [0, 1, 2, 3, 5]


#
# @lcpr case=start
# 6\n[[1,2,5],[2,3,8],[1,5,10]]\n1\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[3,1,3],[1,2,2],[0,3,3]]\n3\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[3,4,2],[1,2,1],[2,3,1]]\n1\n
# @lcpr case=end

#
