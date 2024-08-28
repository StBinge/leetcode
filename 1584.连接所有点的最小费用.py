#
# @lc app=leetcode.cn id=1584 lang=python3
#
# [1584] 连接所有点的最小费用
#
from sbw import *


# @lc code=start
class Bit:
    def __init__(self,n) -> None:
        self.tree=[float('inf')]*n
        self.id=[-1]*n
        self.n=n

    def lowbit(self,x):
        return x&-x

    def query(self,pos):
        res=-1
        mi=float('inf')
        while pos<self.n:
            if mi > self.tree[pos]:
                mi=self.tree[pos]
                res=self.id[pos]
            pos+=self.lowbit(pos)
        return res

    def update(self,pos,val,id):
        while pos>0:
            if val<self.tree[pos]:
                self.tree[pos]=val
                self.id[pos]=id
            pos-=self.lowbit(pos)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)

        edges = []
        
        def build(pos:list):
            pos.sort()
            a=[y-x for (x,y,_) in pos]
            b=sorted(set(a))
            N=len(b)
            bit=Bit(N+1)
            for i in range(n-1,-1,-1):
                poss=bisect.bisect(b,a[i])
                j=bit.query(poss)
                if j!=-1:
                    p1,p2=pos[i][2],pos[j][2]
                    edges.append((dist(points[p1],points[p2]),p1,p2))
                bit.update(poss,pos[i][0]+pos[i][1],i)
        # def build(pos: List[Tuple[int, int, int]]):
        #     pos.sort()
        #     a=[y-x for (x,y,_) in pos]
        #     b = sorted(set(a))
        #     N=len(b)
        #     bit=Bit(N+1)
        #     for i in range(n - 1, -1, -1):
        #         poss = bisect.bisect(b, a[i])
        #         j = bit.query(poss)
        #         if j != -1:
        #             dis = abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1])
        #             edges.append((dis, pos[i][2], pos[j][2]))
        #         bit.update(poss, pos[i][0] + pos[i][1], i)


        pos=[(x,y,i) for i,(x,y) in enumerate(points)]
        build(pos)
        pos=[(y,x,i) for i,(x,y) in enumerate(points)]
        build(pos)
        pos=[(x,-y,i) for i,(x,y) in enumerate(points)]
        build(pos)
        pos=[(-y,x,i) for i,(x,y) in enumerate(points)]
        build(pos)


        edges.sort()
        p = list(range(n))
        size = [1] * n
        roots = n

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return False
            if size[x] > size[y]:
                p[y] = x
                size[x] += size[y]
            else:
                p[x] = y
                size[y] += size[x]
            return True

        ret = 0
        for d, i, j in edges:
            if roots == 1:
                break
            if union(i, j):
                ret += d
                roots -= 1
        return ret


# @lc code=end
assert Solution().minCostConnectPoints([[0, 0], [1, 1], [1, 0], [-1, 1]]) == 4
assert Solution().minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]) == 18
assert (
    Solution().minCostConnectPoints(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]])
    == 20
)
