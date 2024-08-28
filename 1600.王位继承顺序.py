#
# @lc app=leetcode.cn id=1600 lang=python3
#
# [1600] 王位继承顺序
#
from sbw import *
# @lc code=start
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.parents={kingName:[]}
        self.king=kingName
        self.deads=set()

    def birth(self, parentName: str, childName: str) -> None:
        self.parents.setdefault(parentName,[]).append(childName)

    def death(self, name: str) -> None:
        self.deads.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ret=[]
        q=deque([self.king])
        while q:
            parent=q.popleft()
            if parent not in self.deads:
                ret.append(parent)
            for child in reversed(self.parents.get(parent,[])):
                q.appendleft(child) 
        return ret



t= ThroneInheritance("king")# 继承顺序：king
t.birth("king", "andy")# 继承顺序：king > andy
t.birth("king", "bob")# 继承顺序：king > andy > bob
t.birth("king", "catherine")# 继承顺序：king > andy > bob > catherine
t.birth("andy", "matthew")# 继承顺序：king > andy > matthew > bob > catherine
t.birth("bob", "alex")# 继承顺序：king > andy > matthew > bob > alex > catherine
t.birth("bob", "asha")# 继承顺序：king > andy > matthew > bob > alex > asha > catherine
assert t.getInheritanceOrder() ==["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
t.death("bob")# 继承顺序：king > andy > matthew > bob（已经去世）> alex > asha > catherine
assert t.getInheritanceOrder()==["king", "andy", "matthew", "alex", "asha", "catherine"]
# @lc code=end

