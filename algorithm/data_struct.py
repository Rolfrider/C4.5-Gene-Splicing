from abc import ABC, abstractmethod

class Example:

    def __init__(self, gene: str, positive: str):
        self.attributes = gene
        self.positive = positive == '1'


class Node(ABC):

    def __init__(self, level, train_examples: [Example]):
        self.level = level
        self.train_examples = train_examples

    @abstractmethod
    def determine(self, attribiutes) -> bool:
        pass

    def __str__(self):
        return "Level: " + str(self.level)


class Branch(Node):
    def __init__(self, level, train_examples: [Example], spliting_attr: int, children):
        super().__init__(level, train_examples)
        self.children = children
        self.spliting_attr = spliting_attr

    def __str__(self):
        return super().__str__() + " Branch split on index: " + str(self.spliting_attr) + self.children_str()

    def children_str(self):
        string = ""
        for val, node in self.children.items():
            string += "\nFor value: " + str(val) + " have " + str(node)
        return string

    def determine(self, attribiutes): 
        key = attribiutes[self.spliting_attr]
        if key in self.children:
            return self.children[key].determine(attribiutes)
        else:
            return False

    def replace_branch(self, branch, node):
        if all(isinstance(child, Leaf) for child in self.children.values()):
            return
        for key, child in self.children.items():
            if child == branch:
                self.children[key] = node
                return
            elif isinstance(child, Branch):
                child.replace_branch(branch, node)


class Leaf(Node):

    def __init__(self, level, train_examples: [Example], positive: bool):
        super().__init__(level, train_examples)
        self.positive = positive

    def __str__(self):
        return super().__str__() + " Leaf: " + str(self.positive)

    def determine(self, attribiutes):
        return self.positive