#
# @lc app=leetcode.cn id=面试题 03.04 lang=python3
# @lcpr version=30204
#
# [面试题 03.04] 化栈为队
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.front=[]
        self.tail=[]

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.tail.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.front:
            return self.front.pop()
        for i in range(len(self.tail)):
            self.front.append(self.tail.pop())
        return self.front.pop()
    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.front:
            return self.front[-1]
        for i in range(len(self.tail)):
            self.front.append(self.tail.pop())
        return self.front[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.front and not self.tail


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end



