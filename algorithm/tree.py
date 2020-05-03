from algorithm.data_struct import Example
from algorithm.entropy import *

class Tree:

    def __init__(self, training_data: [Example]):
        self.root = Node(0 , training_data)
        
class SplitAtribute:

    def __init__(self, index: int, value: str):
        self.index = index
        self.value = value

    def match(self, example: Example):
        return example.attributes[self.index] == self.value

def build_tree(training_data: [Example]):
    attr_indecies = [i for i in range(0, len(training_data[0].attributes))]
    return id3(attr_indecies, training_data)
    pass

def id3(attr_indecies: [int], examples: [Example]):
    if all(example.positive for example in examples):
        return Leaf(0, True)

    if all(not example.positive for example in examples):
        return Leaf(0, False)

    if not attr_indecies:
        positives, negatives = count_classes(examples)
        return Leaf(0, True) if positives > negatives else Leaf(0, False)

    best_attr = max(attr_indecies, key=lambda attr: inf_gain(attr, examples))

    value_examples = split(best_attr, examples)

    attr_indecies.remove(best_attr)

    children = { val : id3(attr_indecies, exps) for val, exps in value_examples.items() }

    return Branch(0, best_attr, children)



def inf_gain(attr_index: int, examples: [Example]):
    return entropy(examples) - inf(attr_index, examples)

def inf(attr_index: int, examples: [Example]):
    value_examples = split(attr_index, examples)
    examples_count = len(examples)
    return sum( single_inf(attr_examples, examples_count) for attr_examples in value_examples.values())

def split(attr_index: int, examples: [Example]):
    value_examples = dict()
    for exp in examples:
        key = exp.attributes[attr_index]
        value_examples[key] = value_examples.get(key, []) + [exp]
    return value_examples
    
def single_inf(attr_examples: [Example], examples_count: int):
    return (len(attr_examples)/examples_count) * entropy(attr_examples)
        

class Node:

    def __init__(self, level):
        self.level = level

class Branch(Node):
    def __init__(self, level, spliting_attr: int, children):
        super().__init__(level)
        self.children = children
        self.spliting_attr = spliting_attr

    def __str__(self):
        return "Branch split on index: " + str(self.spliting_attr) + self.children_str()

    def children_str(self):
        string = ""
        for val, node in self.children.items():
             string += "\nFor value: " + str(val) + " have " + str(node)
        return string


class Leaf(Node):

    def __init__(self, level, positive: bool):
        super().__init__(level)
        self.positive = positive

    def __str__(self):
        return "Leaf: " + str(self.positive)