class QuadNode:
    def __init__(self, val, isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

    @classmethod
    def build(cls, vals: list | str):
        if isinstance(vals, str):
            vals = eval(vals.replace("null", "None"))
        if not vals:
            return None
        root = QuadNode(vals[0][1])
        cur_level = [root]
        idx = 1
        L = len(vals)
        while idx < L and cur_level:
            next_level = []
            for node in cur_level:
                if idx == L:
                    break
                node.topLeft = QuadNode(vals[idx][1]) if vals[idx] else None
                if node.topLeft:
                    next_level.append(node.topLeft)
                idx += 1

                if idx == L:
                    break
                node.topRight = QuadNode(vals[idx][1]) if vals[idx] else None
                if node.topRight:
                    next_level.append(node.topRight)
                idx += 1

                if idx == L:
                    break
                node.bottomLeft = QuadNode(vals[idx][1]) if vals[idx] else None
                if node.bottomLeft:
                    next_level.append(node.bottomLeft)
                idx += 1

                if idx == L:
                    break
                node.bottomRight = QuadNode(vals[idx][1]) if vals[idx] else None
                if node.bottomRight:
                    next_level.append(node.bottomRight)
                idx += 1
            cur_level = next_level
        
        QuadNode.__set_leaf_flag(root)
        return root
    
    @classmethod
    def __set_leaf_flag(cls,node:'QuadNode'):
        has_child=False
        if node.topLeft:
            has_child=True
            QuadNode.__set_leaf_flag(node.topLeft)
        
        if node.topRight:
            has_child=True
            QuadNode.__set_leaf_flag(node.topRight)
        
        if node.bottomLeft:
            has_child=True
            QuadNode.__set_leaf_flag(node.bottomLeft)
        
        if node.bottomRight:
            has_child=True
            QuadNode.__set_leaf_flag(node.bottomRight)
        
        node.isLeaf=not has_child



if __name__ == "__main__":
    root = QuadNode.build(
        "[[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]"
    )
    pass
