from algorithm.data_struct import Example
from algorithm.entropy import *
from abc import ABC, abstractmethod
from queue import PriorityQueue
from math import sqrt


def build_tree(training_data: [Example]):
    attr_indecies = [i for i in range(0, len(training_data[0].attributes))]
    tree = id3(attr_indecies, training_data)
    print("Before c4.5:")
    print(tree)
    return c45(tree)


def id3(attr_indecies: [int], examples: [Example], level: int = 0):
    if all(example.positive for example in examples):
        return Leaf(level, examples, True)

    if all(not example.positive for example in examples):
        return Leaf(level, examples, False)

    if not attr_indecies:
        positives, negatives = count_classes(examples)
        return Leaf(level, examples, True) if positives > negatives else Leaf(level, examples, False)

    best_attr = max(attr_indecies, key=lambda attr: inf_gain(attr, examples))

    value_examples = split(best_attr, examples)

    attr_indecies.remove(best_attr)

    next_level = level + 1

    children = {val: id3(attr_indecies, exps, next_level)
                for val, exps in value_examples.items()}

    return Branch(level, examples, best_attr, children)


def c45(tree):
    branches = get_branches(tree)
    for branch in sorted(branches, key=lambda x: x.level, reverse=True):
        branch_error = error(branch, branch.train_examples)
        positives, negatives = count_classes(branch.train_examples)
        leaf = Leaf(branch.level, branch.train_examples, True) if positives > negatives else Leaf(
            branch.level, branch.train_examples, False)
        leaf_error = error(leaf, leaf.train_examples)
        if branch_error >= leaf_error:
            tree.replace_branch(branch, leaf)
    return tree


def error(tree, examples):
    error_on_training = training_set_error(tree, examples)
    return estimated_error(error_on_training, len(examples))


def estimated_error(training_error, examples_count):
    return training_error + (sqrt(training_error + training_error**2) / examples_count)


def training_set_error(tree, examples):
    evaluated_well = 0
    for example in examples:
        value = tree.determine(example.attributes)
        if value == example.positive:
            evaluated_well += 1

    return evaluated_well/len(examples)


def get_branches(node, branches=[]):
    if isinstance(node, Leaf):
        return branches
    else:
        branches_and_me = branches + [node]
        for child in node.children.values():
            new_branches = get_branches(child, branches)
            if not new_branches:
                continue
            branches_and_me += new_branches
        return branches_and_me


def inf_gain(attr_index: int, examples: [Example]):
    return entropy(examples) - inf(attr_index, examples)


def inf(attr_index: int, examples: [Example]):
    value_examples = split(attr_index, examples)
    examples_count = len(examples)
    return sum(single_inf(attr_examples, examples_count) for attr_examples in value_examples.values())


def split(attr_index: int, examples: [Example]):
    value_examples = dict()
    for exp in examples:
        key = exp.attributes[attr_index]
        value_examples[key] = value_examples.get(key, []) + [exp]
    return value_examples


def single_inf(attr_examples: [Example], examples_count: int):
    return (len(attr_examples)/examples_count) * entropy(attr_examples)


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
        return self.children[key].determine(attribiutes)

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
