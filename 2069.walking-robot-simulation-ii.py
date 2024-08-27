#
# @lc app=leetcode.cn id=2069 lang=python3
# @lcpr version=30204
#
# [2069] 模拟行走机器人 II
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Robot:

    def __init__(self, width: int, height: int):
        self.pos=[]
        self.dirs=[]
        self.moved=False
        self.idx=0
        for i in range(width):
            self.pos.append([i,0])
            self.dirs.append(0)
        
        for i in range(height-1):
            self.pos.append([width-1,i+1])
            self.dirs.append(1)
        
        for i in range(width-2,-1,-1):
            self.pos.append([i,height-1])
            self.dirs.append(2)
        
        for i in range(height-2,0,-1):
            self.pos.append([0,i])
            self.dirs.append(3)
        
        self.dirs[0]=3

    def step(self, num: int) -> None:
        self.idx=(self.idx+num)%len(self.pos)
        self.moved=True


    def getPos(self) -> List[int]:
        return self.pos[self.idx]

    def getDir(self) -> str:
        if not self.moved:
            return 'East'
        return ["East" ,"North" ,"West" ,"South"][self.dirs[self.idx]]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
# @lc code=end



ops=["Robot", "step", "step", "getPos", "getDir", "step", "step", "step", "getPos", "getDir"]
args=[[6, 3], [2], [2], [], [], [2], [1], [4], [], []]
ansers=eval_list_str('[null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"]')
obj=None
for op,arg,ans in zip(ops,args,ansers):
    if op=='Robot':
        obj=Robot(*arg)
    # elif op=='step':
    #     obj.step(*arg)
    elif ans is not None:
        assert obj.__getattribute__(op)(*arg)==ans
    else:
        obj.__getattribute__(op)(*arg)


#
# @lcpr case=start
# ["Robot", "step", "step", "getPos", "getDir", "step", "step", "step", "getPos", "getDir"][[6, 3], [2], [2], [], [], [2], [1], [4], [], []]\n
# @lcpr case=end

#

