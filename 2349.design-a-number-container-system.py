#
# @lc app=leetcode.cn id=2349 lang=python3
# @lcpr version=30204
#
# [2349] 设计数字容器系统
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class NumberContainers:

    def __init__(self):
        self.slots={}
        self.indices={}

    def change(self, index: int, number: int) -> None:
        self.slots[index]=number
        indices=self.indices.setdefault(number,[])
        heapq.heappush(indices,index)

    def find(self, number: int) -> int:
        indices=self.indices.get(number,[])
        while indices:
            idx=indices[0]
            if self.slots[idx]==number:
                return idx
            heapq.heappop(indices)
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
# @lc code=end
obj=NumberContainers()

ops=["NumberContainers","change","change","find","find","find","change","find","find","change","find","change","change","change","find","find","change","find","change","change","change"]
args=[[],[25,50],[56,31],[50],[50],[43],[30,50],[31],[43],[25,20],[50],[56,43],[68,31],[56,31],[20],[43],[25,43],[43],[56,31],[54,43],[63,43]]
ret=eval_list_str('[null,null,null,25,25,-1,null,56,-1,null,30,null,null,null,25,-1,null,25,null,null,null]')
test_obj(obj,ops,args,ret)

ops=["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
args=[[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
ret=eval_list_str('[null, -1, null, null, null, null, 1, null, 2]')

test_obj(obj,ops,args,ret)



#
# @lcpr case=start
# ["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"][[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]\n
# @lcpr case=end

#

