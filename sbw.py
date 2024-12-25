from typing import List,Optional,Tuple
from collections import deque,Counter,defaultdict
from functools import cache,reduce
from itertools import accumulate,zip_longest
from random import randint
from bisect import bisect,bisect_left,bisect_right
from itertools import pairwise,groupby
import heapq,bisect,math



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def build(cls, nums: list) -> "ListNode":
        dummy = ListNode(0)
        cur = dummy
        for n in nums:
            cur.next = ListNode(n)
            cur = cur.next
        return dummy.next

    def to_list(self):
        cur = self
        nums = []
        while cur:
            nums.append(cur.val)
            cur = cur.next
        return nums
    def print(self):      

        print("->".join(map(str, self.to_list())))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def build(cls, vals):
        if isinstance(vals, str):
            vals = eval(vals.replace("null", "None"))
        if not vals:
            return None
        root = TreeNode(vals[0])
        queue = [root]
        idx = 1
        N = len(vals)
        while queue and idx < N:
            temp = []
            for node in queue:
                if idx == N:
                    break
                node.left = TreeNode(vals[idx]) if vals[idx] != None else None
                if node.left:
                    temp.append(node.left)
                idx += 1
                if idx == N:
                    break
                node.right = TreeNode(vals[idx]) if vals[idx] != None else None
                if node.right:
                    temp.append(node.right)
                idx += 1
            queue = temp
        return root

    def to_str(self):
        if not self:
            return "[null]"
        queue = [self]
        ret = []
        while queue:
            nxt = []
            for node in queue:
                if not node:
                    ret.append(None)
                else:
                    ret.append(node.val)
                    nxt.append(node.left)
                    nxt.append(node.right)
            queue = nxt
        while ret and ret[-1] == None:
            ret.pop()
        return "[" + ",".join(map(str, ret)).replace("None", "null") + "]"

    @property
    def depth(self):
        q=[self,1]
        ret=1
        while q:
            node,d=q.pop()
            ret=max(ret,d)
            if node.left:
                q.append([node.left,d+1])
            if node.right:
                q.append([node.right,d+1])
        return ret
    
    @property
    def extreme_vals(self):
        q=[self]
        ma=float('-inf')
        mi=float('inf')
        while q:
            node=q.pop()
            ma=max(ma,node.val)
            mi=min(mi,node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return [mi,ma]

    def print(self,row_gap,col_gap):
        d=self.depth
        mi,ma=self.extreme_vals
        val_str_len=max(len(mi),len(ma))
    
    def is_same(self,other:'TreeNode'):
        q1=[self]
        q2=[other]
        while q1 and q2:
            n1=q1.pop()
            n2=q2.pop()
            if n1.val!=n2.val:
                return False
            has_left1=n1.left is not None
            has_left2=n2.right is not None
            if has_left1!=has_left2:
                return False
            if has_left1:
                q1.append(n1.left)
                q2.append(n2.left)
            
            has_right1=n1.right is not None
            has_right2=n2.right is not None
            if has_right1!=has_right2:
                return False
            if has_right1:
                q1.append(n1.right)
                q2.append(n2.right)
        return len(q1)==len(q2)
class SortedSet:
    def __init__(self) -> None:
        self.array = []
        self.set = set()

    def add(self, value):
        if value in self.set:
            return
        self.set.add(value)
        self.array.insert(self.bisect_right(value), value)

    def bisect_right(self, value):
        left, right = 0, len(self.array)
        while left < right:
            mid = (left + right) // 2
            x = self.array[mid]
            if x < value:
                left = mid + 1
            else:
                right = mid
        return left

    def bisect_left(self, value):
        left, right = 0, len(self.array)
        x = 0
        while left < right:
            mid = (left + right) // 2
            x = self.array[mid]
            if x > value:
                right = mid
            else:
                left = mid + 1
        return left - 1


def format_array(s: str):
    s = s.replace("null", "None")
    return eval(s)


def eval_list_str(s: str):
    replace_items = [
        ["null", "None"],
        ["false", "False"],
        ["true", "True"],
    ]
    for old, new in replace_items:
        s = s.replace(old, new)
    return eval(s)


def exec_expression(expr: str):
    import re

    expr = re.sub(r",\s+", "\n", expr)
    old_vars=locals().copy()

    exec(expr)
    ret={}
    for k,v in locals().items():
        if k not in old_vars:
            ret[k]=v
    ret.pop('old_vars')
    ret.pop('ret')
    return ret

def assert_test(obj:object,operations:list,args:list,answers:list,skip_offset=1):

    for op,arg,answer in zip(operations[skip_offset:],args[skip_offset:],answers[skip_offset:]):
        ret =obj.__getattribute__(op)(*arg)
        if ret==answer:
            continue
        raise


def is_equal(obj1,obj2):
    if obj1 is None and obj2 is None:
        return True
    elif isinstance(obj1,list):
        for item1,item2 in zip_longest(obj1,obj2):
            if not is_equal(item1,item2):
                return False
        return True
    elif isinstance(obj1,float):
        return abs(obj1-obj2)<=1e-5
    elif isinstance(obj1,ListNode):
        return obj1.to_list()==obj2.to_list()
    elif isinstance(obj1,TreeNode):
        return obj1.to_str()==obj2.to_str()
    else:
        return obj1==obj2

def assert_answer(answer,ret):
    error_msg=f'\nAnswer:{answer}\nRet:{ret}'
    assert is_equal(answer,ret),error_msg


# def assert_input_output(func,expressions:str):
#     pass

def test_obj(cls,operations,args,answers,offset=1):
    obj=cls(*args[0])
    if isinstance(answers,str):
        answers=eval_list_str(answers)
    for i in range(offset,len(operations)):
        method=obj.__getattribute__(operations[i])
        ret=method(*args[i])
        if not is_equal(ret,answers[i]):
            print('Idx:',i)
            print('Op :',operations[i])
            print('Arg:',args[i])
            print('Ret:',ret)
            print('Ans:',answers[i])
            print('Test Failed')
    else:
        print('Test Pass')

if __name__ == "__main__":
    r = exec_expression("grid = [[1,1],[1,2]], row = 0, col = 0, color = 3")
    pass
