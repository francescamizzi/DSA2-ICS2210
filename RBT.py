import random

class Node():
    def __init__(self, number):
        self.number = number
        self.parent = None
        self.left = None
        self.right = None
        self.colour = 1


class Tree():
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.colour = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
        self.rotatesL = 0
        self.rotatesR = 0
        self.nodes = 0

    def rotateL(self, node):
        self.rotatesL += 1
        nodeR = node.right
        node.right = nodeR.left
        if nodeR.left != self.TNULL:
            nodeR.left.parent = node

        nodeR.parent = node.parent
        if node.parent == None:
            self.root = nodeR
        elif node == node.parent.left:
            node.parent.left = nodeR
        else:
            node.parent.right = nodeR
        nodeR.left = node
        node.parent = nodeR

    def rotateR(self, node):
        self.rotatesR += 1
        nodeL = node.left
        node.left = nodeL.right
        if nodeL.right != self.TNULL:
            nodeL.right.parent = node

        nodeL.parent = node.parent
        if node.parent == None:
            self.root = nodeL
        elif node == node.parent.right:
            node.parent.right = nodeL
        else:
            node.parent.left = nodeL
        nodeL.right = node
        node.parent = nodeL

    def insert(self, num):
        node = Node(num)
        node.parent = None
        node.number = num
        node.left = self.TNULL
        node.right = self.TNULL
        node.colour = 1

        j = None
        k = self.root

        while k != self.TNULL:
            j = k
            if node.number < k.number:
                k = k.left
            else:
                k = k.right

        node.parent = j
        if j == None:
            self.root = node
        elif node.number < j.number:
            j.left = node
        else:
            j.right = node

        if node.parent == None:
            node.colour = 0
            return

        if node.parent.parent == None:
            return

        self.insert_balance(node)

        self.nodes += 1

    def insert_balance(self, node):
        while node.parent.colour == 1:
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle.colour == 1:
                    uncle.colour = 0
                    node.parent.colour = 0
                    node.parent.parent.colour = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotateR(node)
                    node.parent.colour = 0
                    node.parent.parent.colour = 1
                    self.rotateL(node.parent.parent)
            else:
                uncle = node.parent.parent.right

                if uncle.colour == 1:
                    uncle.colour = 0
                    node.parent.colour = 0
                    node.parent.parent.colour = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotateL(node)
                    node.parent.colour = 0
                    node.parent.parent.colour = 1
                    self.rotateR(node.parent.parent)
            if node == self.root:
                break
        self.root.colour = 0

    def remove(self, number):
        self.remove_node(self.root, number)

    def remove_node(self, node, key):
        a = self.TNULL
        while node != self.TNULL:
            if node.number == key:
                a = node

            if node.number <= key:
                node = node.right
            else:
                node = node.left

        if a == self.TNULL:
            return

        b = a
        bogc = b.colour
        if a.left == self.TNULL:
            c = a.right
            self.exchange(a, a.right)
        elif (a.right == self.TNULL):
            c = a.left
            self.exchange(a, a.left)
        else:
            b = self.minimum(a.right)
            bogc = b.colour
            c = b.right
            if b.parent == a:
                c.parent = b
            else:
                self.exchange(b, b.right)
                b.right = a.right
                b.right.parent = b

            self.exchange(a, b)
            b.left = a.left
            b.left.parent = b
            b.colour = a.colour
        if bogc == 0:
            self.remove_balance(c)

        self.nodes -= 1

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def exchange(self, x, y):
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.parent = x.parent

    def remove_balance(self, node):
        while node != self.root and node.colour == 0:
            if node == node.parent.left:
                x = node.parent.right
                if x.colour == 1:
                    x.colour = 0
                    node.parent.colour = 1
                    self.rotateL(node.parent)
                    x = node.parent.right

                if x.left.colour == 0 and x.right.colour == 0:
                    x.colour = 1
                    node = node.parent
                else:
                    if x.right.colour == 0:
                        x.left.colour = 0
                        x.colour = 1
                        self.rotateR(x)
                        x = node.parent.right

                    x.colour = node.parent.colour
                    node.parent.colour = 0
                    x.right.colour = 0
                    self.rotateL(node.parent)
                    node = self.root
            else:
                x = node.parent.left
                if x.colour == 1:
                    x.colour = 0
                    node.parent.colour = 1
                    self.rotateR(node.parent)
                    x = node.parent.left

                if x.right.colour == 0 and x.right.colour == 0:
                    x.colour = 1
                    node = node.parent
                else:
                    if x.left.colour == 0:
                        x.right.colour = 0
                        x.colour = 1
                        self.rotateL(x)
                        x = node.parent.left

                    x.colour = node.parent.colour
                    node.parent.colour = 0
                    x.left.colour = 0
                    self.rotateR(node.parent)
                    node = self.root
        node.colour = 0

    def resetCounters(self):
        self.rotatesL = 0
        self.rotatesR = 0


if __name__ == "__main__":
    tree = Tree()
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
        root = tree.insert(num)

    print('----------------------------')
    print('|      After Insertion     |')
    print('----------------------------')

    print("Rotations Left: " + str(tree.rotatesL))
    print("Rotations Right: " + str(tree.rotatesR))
    print("Total Rotations: " + str(tree.rotatesL + tree.rotatesR))
    print("Nodes: " + str(tree.nodes))

    tree.resetCounters()

    for num in Y:
        root = tree.remove(num)

    print('---------------------------')
    print('|      After Deletion     |')
    print('---------------------------')

    print("Rotations Left: " + str(tree.rotatesL))
    print("Rotations Right: " + str(tree.rotatesR))
    print("Total Rotations: " + str(tree.rotatesL + tree.rotatesR))
    print("Nodes: " + str(tree.nodes))
