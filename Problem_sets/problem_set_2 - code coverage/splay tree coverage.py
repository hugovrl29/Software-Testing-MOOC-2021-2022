# TASK:
#
# This is the SplayTree code we saw earlier in the 
# unit. We didn't achieve full statement coverage 
# during the unit, but we will now!
# Your task is to achieve full statement coverage 
# on the SplayTree class. 
# 
# You will need to:
# 1) Write your test code in the test function.
# 2) Press submit. The grader will tell you if you 
#    fail to cover any specific part of the code.
# 3) Update your test function until you cover the 
#    entire code base.
#
# You can also run your code through a code coverage 
# tool on your local machine if you prefer. This is 
# not necessary, however.
# If you have any questions, please don't hesitate 
# to ask in the forums!
from random import randint

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

    def equals(self, node):
        return self.key == node.key

class SplayTree:
    def __init__(self):
        self.root = None
        self.header = Node(None) #For splay()

    def insert(self, key):
        if (self.root == None):
            self.root = Node(key)
            return

        self.splay(key)
        if self.root.key == key:
            # If the key is already there in the tree, don't do anything.
            return

        n = Node(key)
        if key < self.root.key:
            n.left = self.root.left
            n.right = self.root
            self.root.left = None
        else:
            n.right = self.root.right
            n.left = self.root
            self.root.right = None
        self.root = n

    def remove(self, key):
        self.splay(key)
        if self.root is None or key != self.root.key:
            return

        # Now delete the root.
        if self.root.left== None:
            self.root = self.root.right
        else:
            x = self.root.right
            self.root = self.root.left
            self.splay(key)
            self.root.right = x

    def findMin(self):
        if self.root == None:
            return None
        x = self.root
        while x.left != None:
            x = x.left
        self.splay(x.key)
        return x.key

    def findMax(self):
        if self.root == None:
            return None
        x = self.root
        while (x.right != None):
            x = x.right
        self.splay(x.key)
        return x.key

    def find(self, key):
        if self.root == None:
            return None
        self.splay(key)
        if self.root.key != key:
            return None
        return self.root.key

    def isEmpty(self):
        return self.root == None
    
    def splay(self, key):
        l = r = self.header
        t = self.root
        if t is None:
            return
        self.header.left = self.header.right = None
        while True:
            if key < t.key:
                if t.left == None:
                    break
                if key < t.left.key:
                    y = t.left
                    t.left = y.right
                    y.right = t
                    t = y
                    if t.left == None:
                        break
                r.left = t
                r = t
                t = t.left
            elif key > t.key:
                if t.right == None:
                    break
                if key > t.right.key:
                    y = t.right
                    t.right = y.left
                    y.left = t
                    t = y
                    if t.right == None:
                        break
                l.right = t
                l = t
                t = t.right
            else:
                break
        l.right = t.left
        r.left = t.right
        t.left = self.header.right
        t.right = self.header.left
        self.root = t


# Write test code in this function to achieve 
# full statement coverage on the SplayTree class.
def test():
    ###Your code here.
    
    #create a test tree
    test_tree = SplayTree()
    assert test_tree
    
    #check that the test is actually an empty tree
    assert test_tree.isEmpty()
    
    find_x = test_tree.find(9)
    assert find_x == None
    
    #check min and max for empty tree
    assert (test_tree.findMin() == None) and (test_tree.findMax() == None)
    
    #check insertion
    insertion = test_tree.insert(5)
    assert test_tree.isEmpty() == False and test_tree.find(5) == 5 and test_tree.find(6) == None
    
    insertion_2 = test_tree.insert(5)
    assert insertion_2 == None
    
    #check remove
    remove = test_tree.remove(5)
    assert test_tree.find(5) == None
    remove = test_tree.remove(6) #should do nothing
    
    #check min and max in a not empty tree
    for i in range(6):
        insert = test_tree.insert(i)
    insert = test_tree.insert(-1)
    assert test_tree.findMax() == 5 and test_tree.findMin() == -1
    for i in range(6):
        remove = test_tree.remove(i)
    remove = test_tree.remove(-1)
    
    #test splay function where t = None
    test_tree.splay(5)
    
    #test splay function where t = 5 and t.left = None
    for i in range(2):
        test_tree.insert(6-i)
    test_tree.splay(5)
    
    #test splay function where t = 7 and t.right = None
    test_tree.insert(7)
    test_tree.splay(7)
    test_tree.splay(8)
    
    pass

test()

