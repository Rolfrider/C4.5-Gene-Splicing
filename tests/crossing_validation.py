from algorithm.data_struct import *
from algorithm.tree import build_tree
import json

def test_crossing_validation(examples: [Example]):
    set_dividers = [0.05, 0.1, 0.2, 0.25, 0.3, 0.4, 0.5]
    results = []
    for divider in set_dividers:
        results.append(crossing_validation(examples, divider))
    file_name = "results/crossing_validation.json"
    with open(file_name, "w") as file:
        json.dump(results, file)
    

def crossing_validation(examples: [Example], subset_size: float):
    size = len(examples)
    testing_size = (int)(size*subset_size)
    remaining_examples = size
    accuracy = 0
    iteration = 0

    while remaining_examples > 0:
        if remaining_examples >= testing_size:
            testing_set = examples[remaining_examples-testing_size:remaining_examples]
            training_set = examples[:remaining_examples-testing_size] + examples[remaining_examples:]
            remaining_examples = remaining_examples - testing_size
        else:
            testing_set = examples[:remaining_examples]
            training_set = examples[remaining_examples:]
            remaining_examples = 0

        print(len(testing_set))
        print(len(training_set))
        tree = build_tree(training_set)
        results = [tree.determine(x.attributes) for x in testing_set]
        
        accuracy = accuracy + count_accuracy(results, testing_set)
        iteration = iteration + 1
    
    return accuracy/iteration

def count_accuracy(results: [bool], testing_set: Example):
    matching = 0
    for i in range(0, len(results)):
        if results[i] == testing_set[i].positive:
            matching = matching + 1
    print(matching/len(results))
    return matching/len(results)