# autor: Rafał Kwiatkowski
from algorithm.data_struct import Example
from math import log2


def entropy(examples: [Example]) -> float:
    all_no = len(examples)
    clases = count_classes(examples)
    if clases[0] == all_no or clases[1] == all_no:
        return 0
    positive_ratio = clases[0]/all_no
    negative_ratio = clases[1]/all_no
    return -(positive_ratio*log2(positive_ratio)) - (negative_ratio*log2(negative_ratio))

def count_classes(examples: [Example]) -> (int, int):
    positive_no = 0
    negative_no = 0
    for exp in examples:
        if exp.positive:
            positive_no += 1
        else:
            negative_no += 1
    return (positive_no, negative_no)