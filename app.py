from read.read import get_acceptors, get_donors
from algorithm.data_struct import Example
from algorithm.tree import build_tree
from experiments.crossing_validation import test_crossing_validation, crossing_validation

donors = get_donors()
acteptors = get_acceptors()
donors_examples = list(map(lambda x: Example(x[1], x[0]), donors))
acteptors_examples = list(map(lambda x: Example(x[1], x[0]), acteptors))

#print(crossing_validation(donors_examples, 5, build_tree))
test_crossing_validation(acteptors_examples, donors_examples)