#
# @lc app=leetcode.cn id=1032 lang=python3
#
# [1032] 字符流
#
from sbw import *
# @lc code=start
class Dict:
    def __init__(self) -> None:
        self.slots:list[Dict]=[None]*26
        self.ending=False
        self.fail:Dict=None

    def insert(self,word:str):
        cur=self
        for c in word:
            idx=ord(c)-ord('a')
            if cur.slots[idx] is None:
                cur.slots[idx]=Dict()
            cur=cur.slots[idx]
        cur.ending=True
        

    def build(self):
        self.fail=self
        q:deque[Dict]=deque()
        for i in range(26):
            child=self.slots[i]
            if child:
                child.fail=self
                q.append(child)
            else:
                self.slots[i]=self
        while q:
            p=q.popleft()
            p.ending=p.ending or p.fail.ending
            for i in range(26):
                child=p.slots[i]
                if child:
                    child.fail=p.fail.slots[i]
                    q.append(child)
                else:
                    p.slots[i]=p.fail.slots[i]
    # def query(chr:str):


class StreamChecker:

    def __init__(self, words: List[str]):
        self.dict=Dict()
        for word in words:
            self.dict.insert(word)
        self.dict.build()
        self.temp=self.dict


    def query(self, letter: str) -> bool:
        self.temp=self.temp.slots[ord(letter)-ord('a')]
        return self.temp.ending


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
# @lc code=end
streamChecker = StreamChecker(["cd", "f", "kl"])#
assert not streamChecker.query("a")# // 返回 False
assert not streamChecker.query("b")# // 返回 False
assert not streamChecker.query("c")# // 返回n False
assert streamChecker.query("d")# // 返回 True ，因为 'cd' 在 words 中
assert not streamChecker.query("e")# // 返回 False
assert streamChecker.query("f")# // 返回 True ，因为 'f' 在 words 中
assert not streamChecker.query("g")# // 返回 False
assert not streamChecker.query("h")# // 返回 False
assert not streamChecker.query("i")# // 返回 False
assert not streamChecker.query("j")# // 返回 False
assert not streamChecker.query("k")# // 返回 False
assert streamChecker.query("l")# // 返回 True ，因为 'kl' 在 words 中
