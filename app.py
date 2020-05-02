from read.read import get_acceptors, get_donors
from algorithm.data_struct import Example
from algorithm.entropy import calc_entropy

# print(get_acceptors())
# print(get_donors())

examples = [
    Example("", '1'),
    Example("", '0'),
    Example("", '1'),
    Example("", '0'),
    Example("", '1'),
    Example("", '0'),
    Example("", '0')
]

print(calc_entropy(examples))
