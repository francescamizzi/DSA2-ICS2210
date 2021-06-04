import random


class Node(object):
    def __init__(self, num):
        self.number = num
        self.left = None
        self.right = None
        self.height = 1


class Tree(object):

    def __init__(self):
        self.rotatesL = 0
        self.rotatesR = 0
        self.treeHeight = 0
        self.nodes = 0

    def resetCounters(self):
        self.rotatesL = 0
        self.rotatesR = 0

    def height(self, root):
        if not root:
            return 0

        return root.height

    def balance(self, root):
        if not root:
            return 0

        return self.height(root.left) - self.height(root.right)

    def minValue(self, root):
        if root is None or root.left is None:
            return root

        return self.minValue(root.left)

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.number), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def rotateL(self, node):

        self.rotatesL += 1

        nodeR = node.right
        nodeN = nodeR.left

        nodeR.left = node
        node.right = nodeN

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        nodeR.height = 1 + max(self.height(nodeR.left), self.height(nodeR.right))

        return nodeR

    def rotateR(self, node):

        self.rotatesR += 1

        nodeL = node.left
        nodeN = nodeL.right

        nodeL.right = node
        node.left = nodeN

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        nodeL.height = 1 + max(self.height(nodeL.left), self.height(nodeL.right))

        return nodeL

    def ins(self, root, num):
        self.nodes += 1

        if not root:
            return Node(num)
        elif num < root.number:
            root.left = self.ins(root.left, num)
        else:
            root.right = self.ins(root.right, num)

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance(root)

        if balance > 1 and num < root.left.number:
            return self.rotateR(root)

        if balance < -1 and num > root.right.number:
            return self.rotateL(root)

        if balance > 1 and num > root.left.number:
            root.left = self.rotateL(root.left)
            return self.rotateR(root)

        if balance < -1 and num < root.right.number:
            root.right = self.rotateR(root.right)
            return self.rotateL(root)

        return root

    def remove(self, root, num):

        if not root:
            return root

        elif num < root.number:
            root.left = self.remove(root.left, num)

        elif num > root.number:
            root.right = self.remove(root.right, num)

        else:
            if root.left is None:
                t1 = root.right
                root = None
                return t1

            elif root.right is None:
                t2 = root.left
                root = None
                return t2

            t3 = self.minValue(root.right)
            root.number = t3.number
            root.right = self.remove(root.right, t3.number)

        if root is None:
            return root


        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance(root)

        if balance > 1 and self.balance(root.left) >= 0:
            return self.rotateR(root)

        if balance < -1 and self.balance(root.right) <= 0:
            return self.rotateL(root)

        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.rotateL(root.left)
            return self.rotateR(root)

        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.rotateR(root.right)
            return self.rotateL(root)

        return root

    def countNodes(self, root):

        if not root:
            return

        self.countNodes(root.left)
        self.nodes += 1
        self.countNodes(root.right)

    def numOfNodes(self, root):
        self.nodes = 0
        self.countNodes(root)
        return self.nodes


if __name__ == '__main__':
    n = random.randint(1000, 3000)
    X = random.sample(range(-3000, 3000), n)

    m = random.randint(500, 1000)
    Y = random.sample(range(-3000, 3000), m)

    common = 0

    for number in Y:
        if number in X:
            common += 1

    print("Set X contains %d elements" % n)
    print("Set Y contains %d elements" % m)
    print("Sets X and Y have %d elements in common" % common)

    tree = Tree()
    root = None

    for num in X:
        root = tree.ins(root, num)

    print('----------------------------')
    print('|      After Insertion     |')
    print('----------------------------')

    print("Rotations Left: " + str(tree.rotatesL))
    print("Rotations Right: " + str(tree.rotatesR))
    print("Total Rotations: " + str(tree.rotatesL + tree.rotatesR))
    print("Tree Height: " + str(tree.height(root)))
    print("Nodes: " + str(tree.numOfNodes(root)))

    tree.resetCounters()

    for num in Y:
        root = tree.remove(root, num)

    print('---------------------------')
    print('|      After Deletion     |')
    print('---------------------------')

    print("Rotations Left: " + str(tree.rotatesL))
    print("Rotations Right: " + str(tree.rotatesR))
    print("Total Rotations: " + str(tree.rotatesL + tree.rotatesR))
    print("Tree Height: " + str(tree.height(root)))
    print("Nodes: " + str(tree.numOfNodes(root)))

