class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

        # this is a node of the tree , which contains info as data, left , right
'''


def lca(root: Node, v1: int, v2: int):
    """Shane's solution"""

    def get_path(v: int, v_path: list[Node]):
        v_cur = root

        while v_cur.info != v:
            if v > v_cur.info:
                v_cur = v_cur.right
            elif v < v_cur.info:
                v_cur = v_cur.left
            v_path.append(v_cur)

    v1_path = [root]
    v2_path = [root]
    get_path(v1, v1_path)
    get_path(v2, v2_path)

    v_common = [x for x in v1_path if x in set(v2_path)]
    return v_common[-1]


def other_lca(root: Node, v1: int, v2: int) -> Node:
    """Anton's solution"""
    curr_node = root
    while True:
        if (v1 < curr_node.info) and (v2 < curr_node.info):
            curr_node = curr_node.left
        elif (v1 > curr_node.info) and (v2 > curr_node.info):
            curr_node = curr_node.right
        else:
            return curr_node


tree = BinarySearchTree()
"""
6
4 2 3 1 7 6

1 7
"""
t = 6

arr = list(map(int, "4 2 3 1 7 6".split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, "1 3".split()))

ans = other_lca(tree.root, v[0], v[1])
print(ans.info)
