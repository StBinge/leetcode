#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#
# @lc code=start
class Node:
    def __init__(self,val) -> None:
        self.val=val
        self.prev=None
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.head=Node(0)
        self.tail=Node(0)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.count=0

    def get(self, index: int) -> int:
        if index<0 or index>=self.count:
            return -1
        cur=self.head.next
        while index:
            cur=cur.next
            index-=1
        return cur.val
    
    def addAtHead(self, val: int) -> None:
        node=Node(val)
        node.next=self.head.next
        node.next.prev=node
        node.prev=self.head
        self.head.next=node
        self.count+=1

    def addAtTail(self, val: int) -> None:
        node=Node(val)
        node.prev=self.tail.prev
        node.prev.next=node
        node.next=self.tail
        self.tail.prev=node
        self.count+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.count or index<0:
            return
        cur=self.head
        while index:
            cur=cur.next
            index-=1
        node=Node(val)
        node.next=cur.next
        node.next.prev=node
        node.prev=cur
        cur.next=node
        self.count+=1

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.count:
            return
        cur=self.head
        while index:
            cur=cur.next
            index-=1
        cur.next=cur.next.next
        cur.next.prev=cur
        self.count-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

linked=MyLinkedList()
linked.addAtHead(9)
assert linked.get(1)==-1
linked.addAtIndex(1,1)
linked.addAtIndex(1,7)
linked.deleteAtIndex(1)
linked.addAtHead(7)
linked.addAtHead(4)
linked.deleteAtIndex(1)
linked.addAtIndex(1,4)
linked.addAtHead(2)
linked.deleteAtIndex(5)
