from algorithm.data_struct import *
from algorithm.tree import build_tree
import json

def test_crossing_validation(examples: [Example]):
    iteration = 3
    set_dividers = [0.2, 0.25, 0.5]
    results = []
    for divider in set_dividers:
        result = 0
        for i in range(0, iteration):
            result = result + crossing_validation(examples, divider)
        results.append(result)
    file_name = "results/crossing_validation.json"
    with open(file_name, "w") as file:
        json.dump(results, file)
    

def crossing_validation(examples: [Example], testing: float):
    size = len(examples)
    testing_size = (int)(size*testing)
    remaining_examples = size
    accuracy = 0
    iteration = 0

    while remaining_examples > 0:
        if remaining_examples > testing_size:
            testing_set = examples[remaining_examples-testing_size:remaining_examples]
            training_set = examples[:remaining_examples-testing_size]
            training_set.extend(examples[remaining_examples:])
            remaining_examples = remaining_examples - testing_size
        else:
            testing_set = examples[0:remaining_examples]
            training_set = examples[remaining_examples:]
            remaining_examples = 0

        #print(len(testing_set))
        #print(len(training_set))
        tree = build_tree(training_set)
        results = [tree.determine(x.attributes) for x in testing_set]
        
        accuracy = accuracy + count_accuracy(results)
        iteration = iteration + 1
    
    return accuracy/iteration

def count_accuracy(results: [bool]):
    positive = 0
    for example in results:
        if example == True:
            positive = positive + 1
    #print(positive/len(results))
    return positive/len(results)