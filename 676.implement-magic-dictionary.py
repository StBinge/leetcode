#
# @lc app=leetcode.cn id=676 lang=python3
# @lcpr version=30204
#
# [676] 实现一个魔法字典
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class MagicDictionary:

    def __init__(self):
        self.dict=None

    def buildDict(self, dictionary: List[str]) -> None:
        self.dict=dictionary


    
    def search(self, searchWord: str) -> bool:
        N=len(searchWord)
        for word in self.dict:
            if N!=len(word):
                continue
            dif=sum(x!=y for x,y in zip(word,searchWord))
            if dif==1:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
# @lc code=end
obj=MagicDictionary()
ops=["MagicDictionary", "buildDict", "search", "search", "search", "search"]
args=[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
answers='[null, null, false, true, false, false]'
test_obj(obj,ops,args,answers)

