#
# @lc app=leetcode.cn id=1472 lang=python3
#
# [1472] 设计浏览器历史记录
#
from sbw import *
# @lc code=start
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history=[homepage]
        self.idx=0
        self.l=1

    def visit(self, url: str) -> None:
        self.idx+=1
        self.l=self.idx+1
        if self.idx==len(self.history):
            self.history.append(url)
        else:
            self.history[self.idx]=url


    def back(self, steps: int) -> str:
        self.idx=max(0,self.idx-steps)
        return self.history[self.idx]

    def forward(self, steps: int) -> str:
        self.idx=min(self.l-1,self.idx+steps)
        return self.history[self.idx]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# @lc code=end
obj=BrowserHistory('esgriv.com')
assert_test(obj,["BrowserHistory","visit","visit","back","visit","forward","visit","visit","forward","visit","back","visit","visit","forward"],[["esgriv.com"],["cgrt.com"],["tip.com"],[9],["kttzxgh.com"],[7],["crqje.com"],["iybch.com"],[5],["uun.com"],[10],["hci.com"],["whula.com"],[10]],eval_list_str('[null,null,null,"esgriv.com",null,"kttzxgh.com",null,null,"iybch.com",null,"esgriv.com",null,null,"whula.com"]'))

obj=BrowserHistory("leetcode.com")
assert_test(obj,["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"],[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]],eval_list_str('[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]'))
