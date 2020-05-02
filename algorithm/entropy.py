from algorithm.data_struct import Example
from math import log2


def calc_entropy(examples: [Example]) -> float:
    # TODO: do sth when ratio is 0
    all_no = len(examples)
    positive_ratio = sum(1 for exp in examples if exp.positive)/all_no
    negative_ratio = sum(1 for exp in examples if not exp.positive)/all_no
    return -(positive_ratio*log2(positive_ratio)) - (negative_ratio*log2(negative_ratio))
