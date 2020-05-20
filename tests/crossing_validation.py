from algorithm.data_struct import *
from algorithm.tree import build_tree
import json

def test_crossing_validation(acteptors_examples: [Example], donors_examples: [Example]):
    set_dividers = [0.05, 0.1, 0.2, 0.25, 0.3, 0.4, 0.5]
    acteptors_results = []
    donors_results = []
    for divider in set_dividers:
        acteptors_results.append(crossing_validation(acteptors_examples, divider))
        donors_results.append(crossing_validation(donors_examples, divider))
    file_name = "results/aceptors_crossing_validation.json"
    with open(file_name, "w") as file:
        json.dump(acteptors_results, file)
    file_name = "results/donors_crossing_validation.json"
    with open(file_name, "w") as file:
        json.dump(donors_results, file)
    

def crossing_validation(examples: [Example], subset_size: float):
    size = len(examples)
    testing_size = (int)(size*subset_size)
    remaining_examples = size
    accuracy = 0
    iteration = 0

    while remaining_examples > 0:
        if remaining_examples >= testing_size:
            start_index = remaining_examples-testing_size
            testing_set = examples[start_index:remaining_examples]
            training_set = examples[:start_index] + examples[remaining_examples:]
            remaining_examples = start_index
        else:
            testing_set = examples[:remaining_examples]
            training_set = examples[remaining_examples:]
            remaining_examples = 0

        print(len(testing_set))
        print(len(training_set))
        tree = build_tree(training_set)
        results = [tree.determine(x.attributes) for x in testing_set]
        
        accuracy += count_accuracy(results, testing_set)
        iteration += 1
    
    return accuracy/iteration

def count_accuracy(results: [bool], testing_set: Example):
    matching = 0
    for i in range(0, len(results)):
        if results[i] == testing_set[i].positive:
            matching += 1
    print(matching/len(results))
    return matching/len(results)