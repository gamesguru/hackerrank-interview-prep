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
"""
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
"""


def height(root):

    h = 0
    q = []
    q.append(root)

    while True:
        n_q = len(q)
        if n_q == 0:
            return h - 1
        h += 1

        while n_q > 0:
            node = q.pop(0)
            n_q -= 1

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


tree = BinarySearchTree()
a = [int(x) for x in "3 5 2 1 4 6 7".split()]
for i in a:
    tree.create(i)

print(height(tree.root))
