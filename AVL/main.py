class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class Tree(object):
    def height(self, root):
        if not root:
            return 0

        return root.height

    def balance(self, root):
        if not root:
            return 0

        return self.height(root.left) - self.getHeight(root.right)

    def minValue(self, root):
        if root is None or root.left is None:
            return root

        return self.getMinValueNode(root.left)

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def rotateL(self, node):

        nodeR = node.right
        nodeN = nodeR.left

        # Perform rotation
        nodeR.left = node
        node.right = nodeN

        # Update heights
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        nodeR.height = 1 + max(self.height(nodeR.left), self.height(nodeR.right))

        # Return the new root
        return nodeR

    def rotateR(self, node):

        nodeL = node.left
        nodeN = y.right

        # Perform rotation
        nodeL.right = node
        node.left = nodeN

        # Update heights
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        nodeL.height = 1 + max(self.height(nodeL.left), self.height(nodeL.right))

        # Return the new root
        return nodeL
