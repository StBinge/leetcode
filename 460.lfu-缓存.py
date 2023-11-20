#
# @lc app=leetcode.cn id=460 lang=python3
#
# [460] LFU 缓存
#

# @lc code=start
class Node:
    def __init__(self,val:int,prev:'Node'=None,nxt:'Node'=None) -> None:
        self.val=val
        self.prev=prev
        self.next=nxt

# class LinkNode(Node):
#     def __init__(self,val, prev: Node = None, nxt: Node = None) -> None:
#         super().__init__(prev, nxt)
#         self.val=val

class CountNode(Node):
    def __init__(self, val: int, prev: Node = None, nxt: Node = None) -> None:
        super().__init__(val, prev, nxt)
        self.keys:dict[int:Node]={}
        self.head=Node(-1)
        self.tail=Node(-1)
        self.head.next=self.tail
        self.tail.prev=self.head
    
    def append_node(self,count:int):
        node=CountNode(count)
        node.next=self.next
        self.next=node
        node.prev=self
        node.next.prev=node
    
    def insert_key(self,key:int):
        node=Node(key)
        node.next=self.head.next
        self.head.next=node
        node.prev=self.head
        node.next.prev=node
        self.keys[key]=node
    
    def remove_key(self,key:int):
        node=self.keys[key]
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
        del self.keys[key]
        self.remove_self()
    
    def remove_oldest(self):
        key=self.tail.prev.val
        self.remove_key(self.tail.prev.val)
        return key

    # def get_val(self,key:int):
    #     node=self.keys[key]
    #     val=node.val
    #     self.remove_key(key)
    #     return val

    def remove_self(self):
        if len(self.keys)>0:
            return
        prev,nxt=self.prev,self.next
        prev.next=nxt
        nxt.prev=prev
        del self

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.kv={}
        self.nodes:dict[int,CountNode]={}
        self.head=CountNode(0)
        self.tail=CountNode(10**10)
        self.head.next=self.tail
        self.tail.prev=self.head

    def _add_freq(self,key):
        node=self.nodes[key]
        cnt=node.val
        if node.next.val!=cnt+1:
            node.append_node(cnt+1)
        node.next.insert_key(key)
        self.nodes[key]=node.next
        node.remove_key(key)

    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1
        self._add_freq(key)
        return self.kv[key]

    def put(self, key: int, value: int) -> None:
        node=self.nodes.get(key,None)
        if not node:
            if len(self.nodes)==self.capacity:
                old_key=self.head.next.remove_oldest()
                del self.kv[old_key]
                del self.nodes[old_key]                
            self.kv[key]=value

            if self.head.next.val!=1:
                self.head.append_node(1)
            self.head.next.insert_key(key)
            self.nodes[key]=self.head.next
            return
        
        self.kv[key]=value
        self._add_freq(key)


        



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
lfu=LFUCache(2)
lfu.put(1,1)
lfu.put(2,2)
assert lfu.get(1)==1
lfu.put(3,3)
assert lfu.get(2)==-1
assert lfu.get(3)==3
lfu.put(4,4)
assert lfu.get(1)==-1
assert lfu.get(3)==3
assert lfu.get(4)==4




