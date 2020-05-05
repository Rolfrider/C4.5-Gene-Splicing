from read.read import get_acceptors, get_donors
from algorithm.data_struct import Example
from algorithm.tree import build_tree

# print(get_acceptors())
# print(get_donors())

examples = [
    Example("EWA", '1'),
    Example("ADA", '0'),
    Example("OLA", '0'),
    Example("IGA", '0'),
    Example("ALA", '1'),
    Example("IZA", '0'),
    Example("IDA", '0')
]
tree = build_tree(examples)
result = tree.determine("EWA")
print(result)
# print(tree)
