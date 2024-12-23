#
# @lc app=leetcode.cn id=LCR 125 lang=python3
# @lcpr version=30204
#
# [LCR 125] 图书整理 II
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class CQueue:

    def __init__(self):
        self.q=deque()

    def appendTail(self, value: int) -> None:
        self.q.append(value)

    def deleteHead(self) -> int:
        if self.q:
            return self.q.popleft()
        return -1


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
# @lc code=end



#
# @lcpr case=start
# ["BookQueue", "push", "push", "pop"][[], [1], [2], []]\n
# @lcpr case=end

#

