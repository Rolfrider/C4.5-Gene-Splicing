from read.read import get_acceptors, get_donors
from algorithm.data_struct import Example
from algorithm.tree import build_tree

# print(get_acceptors())
# print(get_donors())
donors = get_donors()
examples = list(map(lambda x: Example(x[1], x[0]), donors))
# examples = [
#     Example("EWAASDWAS", '1'),
#     Example("ADAKNBJHK", '1'),
#     Example("OJNKJNKLA", '0'),
#     Example("IGBJKNJKA", '0'),
#     Example("ALKJKKJFA", '1'),
#     Example("IZBCVXDFA", '0'),
#     Example("IDMOKMKJA", '0'),
#     Example("ALMOKMKJA", '0'),
#     Example("IDMOKPKJA", '1')
# ]
tree = build_tree(examples)
# result = tree.determine("EWA")
print("After c4.5")
print(tree)
# for branch in sorted(tree, key=lambda x: x.level, reverse=True):
#     print(branch)
