#
# @lc app=leetcode.cn id=1157 lang=python3
#
# [1157] 子数组中占绝大多数的元素
#
from sbw import *
# @lc code=start



class Node:
    def __init__(self,val,cnt) -> None:
        self.val=val
        self.cnt=cnt
    
    def __iadd__(self,other:'Node'):
        if self.val==other.val:
            self.cnt+=other.cnt
        elif self.cnt>=other.cnt:
            self.cnt-=other.cnt
        else:
            self.val=other.val
            self.cnt=other.cnt-self.cnt
        return self

class MajorityChecker:
    K=20
    def __init__(self, arr: List[int]):
        self.arr=arr
        self.slot=defaultdict(list)
        self.n=len(arr)
        for i,a in enumerate(arr):
            self.slot[a].append(i)
        self.tree=[Node(0,0) for _ in range(4*self.n)]
        self.__build(0,0,self.n-1)

    def __build(self, idx: int, l: int, r: int):
        arr_ = self.arr
        tree_ = self.tree

        if l == r:
            tree_[idx] = Node(arr_[l], 1)
            return
        
        mid = (l + r) // 2
        self.__build(idx * 2 + 1, l, mid)
        self.__build(idx * 2 + 2, mid + 1, r)
        tree_[idx] += tree_[idx * 2 + 1]
        tree_[idx] += tree_[idx * 2 + 2]


    
    def __query(self,idx,l,r,ql,qr,node:Node):
        if ql>r or qr<l:
            return
        if ql<=l and r<=qr:
            node+=self.tree[idx]
            return
        mid=(l+r)//2
        self.__query(idx*2+1,l,mid,ql,qr,node)
        self.__query(idx*2+2,mid+1,r,ql,qr,node)


    def query(self, left: int, right: int, threshold: int) -> int:
        ans=Node(0,0)
        self.__query(0,0,self.n-1,left,right,ans)
        # length=right-left+1
        x=ans.val
        pos=self.slot[x]
        cnt=bisect_right(pos,right)-bisect_left(pos,left)
        if cnt>=threshold:
            return x
        return -1




# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
# @lc code=end
arr=[1,1,1,1,1,2,2,2,2,2,2,1,1,1,1,1]
obj = MajorityChecker(arr)
assert obj.query(3,12,6)==2
