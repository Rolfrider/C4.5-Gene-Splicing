from algorithm.data_struct import *
from algorithm.tree import build_tree
import json

def test_crossing_validation(acteptors_examples: [Example], donors_examples: [Example]):
    set_dividers = [0.05, 0.1, 0.2, 0.25, 0.3, 0.4, 0.5]
    acteptors_results = []
    donors_results = []
    for divider in set_dividers:
        acteptors_results.append(((str)(divider), crossing_validation(acteptors_examples, divider)))
        donors_results.append(((str)(divider), crossing_validation(donors_examples, divider)))
    file_name = "results/aceptors_crossing_validation.json"
    with open(file_name, "w") as file:
        json.dump(acteptors_results, file)
    file_name = "results/donors_crossing_validation.json"
    with open(file_name, "w") as file:
        json.dump(donors_results, file)
    

def crossing_validation(examples: [Example], subset_size: float):
    size = len(examples)
    testing_set_size = (int)(size*subset_size)
    remaining_examples = size
    accuracy = 0
    iteration = 0

    while remaining_examples > 0:
        if remaining_examples >= testing_set_size:
            testing_set_start_index = remaining_examples-testing_set_size
            testing_set = examples[testing_set_start_index:remaining_examples]
            training_set = examples[:testing_set_start_index] + examples[remaining_examples:]
            remaining_examples = testing_set_start_index
        else:
            testing_set = examples[:remaining_examples]
            training_set = examples[remaining_examples:]
            remaining_examples = 0

        print("Testing set size: " + str(len(testing_set)))
        print("Training set size: " + str(len(training_set)))
        tree = build_tree(training_set)
        print("Tree after C4.5:")
        print(tree)
        results = [tree.determine(x.attributes) for x in testing_set]
        
        accuracy += count_accuracy(results, testing_set)
        iteration += 1
    
    return accuracy/iteration

def count_accuracy(results: [bool], testing_set: Example):
    matching = 0
    for i in range(0, len(results)):
        if results[i] == testing_set[i].positive:
            matching += 1
    print("Tree answers matching: " + str(matching/len(results)))
    print()
    return matching/len(results)