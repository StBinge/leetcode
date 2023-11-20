#
# @lc app=leetcode.cn id=432 lang=python3
#
# [432] 全 O(1) 的数据结构
#

# @lc code=start
class Node:
    def __init__(self,key:str='',cnt:int=0,pre:'Node'=None,next:'Node'=None) -> None:
        self.cnt=cnt
        self.keys={key}
        self.pre=pre
        self.next=next
    
    def insert(self,node:'Node'):
        nxt=self.next
        self.next=node
        node.pre=self
        if nxt:
            node.next=nxt
            nxt.pre=node
    
    def remove(self):
        self.pre.next=self.next
        self.next.pre=self.pre

class AllOne:

    def __init__(self):
        self.head=Node('',0)
        self.tail=Node('',float('inf'))
        self.head.next=self.tail
        self.tail.pre=self.head
        self.nodes:dict[str,Node]={}

    def inc(self, key: str) -> None:
        if key not in self.nodes:
            node=None
            if self.head.next.cnt==1:
                node=self.head.next
                node.keys.add(key)
            else:
                node=Node(key,1)
                self.head.insert(node)
            self.nodes[key]=node
            return
        
        cur_node=self.nodes[key]
        node=None
        if cur_node.next.cnt==cur_node.cnt+1:
            node=cur_node.next
            node.keys.add(key)
        else:
            node=Node(key,cur_node.cnt+1)
            cur_node.insert(node)
        self.nodes[key]=node
        cur_node.keys.remove(key)
        if len(cur_node.keys)==0:
            cur_node.remove()


    def dec(self, key: str) -> None:
        cur_node=self.nodes[key]
        node=None
        if cur_node.pre.cnt==cur_node.cnt-1:
            node=cur_node.pre
            node.keys.add(key)
        else:
            node=Node(key,cur_node.cnt-1)
            cur_node.pre.insert(node)
        self.nodes[key]=node

        cur_node.keys.remove(key)
        if len(cur_node.keys)==0:
            cur_node.remove()

    def getMaxKey(self) -> str:
        if self.tail.pre==self.head:
            return ''
        for key in self.tail.pre.keys:
            return key

    def getMinKey(self) -> str:
        if self.head.next==self.tail:
            return ''
        for key in self.head.next.keys:
            return key


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# @lc code=end

