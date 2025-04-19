# explanations for member functions are provided in requirements.py
from __future__ import annotations
import math

class FibNode:
    def __init__(self, val: int):
        self.val = val
        self.parent = None
        self.children = []
        self.flag = False
        self.degree = 0

    def get_value_in_node(self):
        return self.val

    def get_children(self):
        return self.children

    def get_flag(self):
        return self.flag

    def __eq__(self, other: FibNode):
        return self.val == other.val

class FibHeap:
    def __init__(self):
        # you may define any additional member variables you need
        self.roots = []
        self.min = None
        self.n = 0

    def get_roots(self) -> list:
        return self.roots

    def insert(self, val: int) -> FibNode:
        new_node = FibNode(val)
        self.roots.append(new_node)
        self.n += 1

        if self.min is None or new_node.val < self.min.val:
            self.min = new_node
        
        return new_node
        
    def delete_min(self) -> None:
        if self.min is None:
                return

        for child in self.min.children:
            self.roots.append(child)
            child.parent = None

        self.roots.remove(self.min)

        if not self.roots:
            self.min = None
        else:
            self.min = self.roots[0]
            self.consolidated()

    def consolidated(self):
        ax = [None] * int(math.log(self.n) * 2)

        for root in self.roots[:]:  
            i = root
            deg = i.degree
            while ax[deg] is not None:
                j = ax[deg]
                if i.val > j.val:
                    i, j = j, i  
                self.link(j, i)
                ax[deg] = None
                deg += 1
            ax[deg] = i

        self.roots = []
        self.min = None
        for node in ax:
            if node is not None:
                self.roots.append(node)
                if self.min is None or node.val < self.min.val:
                    self.min = node

    def link(self, cld: FibNode, prt: FibNode) -> None:
        self.roots.remove(cld)
        prt.children.append(cld)
        cld.parent = prt
        prt.degree += 1
        prt.flag = False

    def find_min(self) -> FibNode:
        return self.min

    def decrease_priority(self, node: FibNode, new_val: int) -> None:
        node.val = new_val
        parent = node.parent

        if parent and node.val < parent.val:
            self.cutting(node, parent)
            self.cascadecut(parent)

        if node.val < self.min.val:
            self.min = node

    def cutting(self, node: FibNode, parent: FibNode):
        parent.children.remove(node)
        parent.degree -= 1
        node.parent = None
        self.roots.append(node)
        node.flag = False

    def cascadecut(self, node: FibNode):
        parent = node.parent
        if parent:
            if not node.flag:
                node.flag = True
            else:
                self.cutting(node, parent)
                self.cascadecut(parent)

    # feel free to define new methods in addition to the above
    # fill in the definitions of each required member function (above),
    # and for any additional member functions you define
