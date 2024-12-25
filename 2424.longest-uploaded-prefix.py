#
# @lc app=leetcode.cn id=2424 lang=python3
# @lcpr version=30204
#
# [2424] 最长上传前缀
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class LUPrefix:

    def __init__(self, n: int):
        self.cnt=[False]*(n+1)
        self.low=1
        self.n=n

    def upload(self, video: int) -> None:
        self.cnt[video]=True

    def longest(self) -> int:
        while self.low<=self.n and  self.cnt[self.low]:
            self.low+=1
        return self.low-1


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
# @lc code=end
test_obj(LUPrefix,["LUPrefix","longest","upload","upload","longest","upload","longest","upload","longest","upload","longest","upload","upload","upload","longest","upload","upload","longest","upload","upload","upload","upload","longest","upload","upload","upload","longest","upload","upload","upload","longest","upload","upload","upload","longest","upload","upload","upload","longest","upload","upload","upload","upload","longest","upload","upload","longest","upload","longest","upload","longest","upload","longest","upload","upload","longest","upload","upload","longest","upload","upload","upload","upload","upload","longest","upload","longest","upload","longest","upload","longest","upload","longest","upload","longest","upload","longest","upload","upload","longest","upload","upload","longest","upload","longest","upload","upload","longest","upload","longest","upload","upload","upload","upload","longest","upload","longest","upload","longest","upload","longest","upload","upload","longest","upload","upload","longest","upload","longest","upload","upload","upload","upload","longest","upload","upload","longest","upload","upload","longest","upload","longest","upload","longest","upload","longest","upload","longest","upload","upload","longest","upload","longest","upload","upload","longest","upload","longest","upload","upload","longest"],[[90],[],[14],[63],[],[69],[],[76],[],[46],[],[68],[33],[15],[],[85],[89],[],[9],[23],[47],[67],[],[2],[26],[82],[],[42],[60],[54],[],[74],[21],[30],[],[78],[10],[19],[],[38],[6],[88],[48],[],[1],[62],[],[39],[],[12],[],[37],[],[75],[36],[],[40],[34],[],[52],[80],[58],[24],[3],[],[27],[],[4],[],[32],[],[87],[],[50],[],[66],[],[43],[35],[],[49],[11],[],[65],[],[8],[57],[],[71],[],[61],[17],[51],[70],[],[73],[],[16],[],[31],[],[83],[79],[],[22],[25],[],[7],[],[45],[5],[41],[77],[],[28],[55],[],[53],[59],[],[29],[],[72],[],[56],[],[81],[],[86],[18],[],[13],[],[64],[90],[],[84],[],[20],[44],[]],'[null,0,null,null,0,null,0,null,0,null,0,null,null,null,0,null,null,0,null,null,null,null,0,null,null,null,0,null,null,null,0,null,null,null,0,null,null,null,0,null,null,null,null,0,null,null,2,null,2,null,2,null,2,null,null,2,null,null,2,null,null,null,null,null,3,null,3,null,4,null,4,null,4,null,4,null,4,null,null,4,null,null,4,null,4,null,null,4,null,4,null,null,null,null,4,null,4,null,4,null,4,null,null,4,null,null,4,null,4,null,null,null,null,12,null,null,12,null,null,12,null,12,null,12,null,12,null,12,null,null,12,null,19,null,null,19,null,19,null,null,90]')
test_obj(LUPrefix,["LUPrefix", "upload", "longest", "upload", "longest", "upload", "longest"],[[4], [3], [], [1], [], [2], []],'[null, null, 0, null, 1, null, 3]')


#
# @lcpr case=start
# ["LUPrefix", "upload", "longest", "upload", "longest", "upload", "longest"][[4], [3], [], [1], [], [2], []]\n
# @lcpr case=end

#

