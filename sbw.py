from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @classmethod
    def build(cls,nums:list)->'ListNode':
        dummy=ListNode(0)
        cur=dummy
        for n in nums:
            cur.next=ListNode(n)
            cur=cur.next
        return dummy.next
    
    def display(self):
        cur=self
        nums=[]
        while cur:
            nums.append(cur.val)
            cur=cur.next

        print('->'.join(map(str,nums)))

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def build(cls,vals:list|str):
        if isinstance(vals,str):
            vals=eval(vals.replace('null','None'))
        if not vals:
            return None
        root=TreeNode(vals[0])
        queue=[root]
        idx=1
        N=len(vals)
        while queue and idx<N:
            temp=[]
            for node in queue:
                if idx==N:
                    break
                node.left=TreeNode(vals[idx]) if vals[idx]!=None else None
                if node.left:
                    temp.append(node.left)
                idx+=1
                if idx==N:
                    break
                node.right=TreeNode(vals[idx]) if vals[idx]!=None else None
                if node.right:
                    temp.append(node.right)
                idx+=1
            queue=temp
        return root
            
                    
    
    def to_str(self):
        if not self:
            return '[null]'
        queue=[self]
        ret=[]
        while queue:
            nxt=[]
            for node in queue:
                if not node:
                    ret.append(None)
                else:
                    ret.append(node.val)
                    nxt.append(node.left)
                    nxt.append(node.right)
            queue=nxt
        while ret and ret[-1]==None:
            ret.pop()
        return '['+','.join(map(str,ret)).replace('None','null')+']'

    def print(self):
        print(self.to_str())


class SortedSet:
    def __init__(self) -> None:
        self.array=[]
        self.set=set()
    
    def add(self,value):
        if value in self.set:
            return
        self.set.add(value)
        self.array.insert(self.bisect_right(value),value)

    def bisect_right(self,value):
        left,right=0,len(self.array)
        while left<right:
            mid=(left+right)//2
            x=self.array[mid]
            if x<value:
                left=mid+1
            else:
                right=mid
        return left
    
    def bisect_left(self,value):
        left,right=0,len(self.array)
        x=0
        while left<right:
            mid=(left+right)//2
            x=self.array[mid]
            if x>value:
                right=mid
            else:
                left=mid+1
        return left-1




if __name__ == '__main__':
    # root=ListNode.build([1,2,3,4,5])
    # root.display()
    root=TreeNode.build([3,4,5,1,3,None,1])
    print(root.to_str())
    # values=[1,3,5,3,4,2,9,3,8]
    # ss=SortedSet()
    # for v in values:
    #     print(f'v:{v},left  index:{ss.bisect_left(v)}')
    #     print(f'v:{v},right index:{ss.bisect_right(v)}')
    #     ss.add(v)
    #     print(ss.array)
    pass