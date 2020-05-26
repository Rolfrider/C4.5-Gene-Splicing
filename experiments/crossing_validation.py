#autor: Franciszek Sioma
from algorithm.data_struct import *
from algorithm.tree import build_tree, build_tree_c45
import json
import random
import matplotlib.pyplot as plt

def test_crossing_validation(acteptors_examples: [Example], donors_examples: [Example]):
    k = 10
    iteration = 100
    
    a_result = 0
    d_result = 0
    a_result_id3 = 0
    d_result_id3 = 0
    for i in range(0, iteration):
        a_result += crossing_validation(acteptors_examples, k, build_tree_c45)
        d_result += crossing_validation(donors_examples, k, build_tree_c45)
        a_result_id3 += crossing_validation(acteptors_examples, k, build_tree)
        d_result_id3 += crossing_validation(donors_examples, k, build_tree)
        
    acteptors_results = (str(k), a_result/iteration)
    donors_results = (str(k), d_result/iteration)
    acteptors_results_id3 = (str(k), a_result_id3/iteration)
    donors_results_id3 = (str(k), d_result_id3/iteration)
    
    save_results(acteptors_results, "c45", "acteptors")
    save_results(donors_results, "c45", "donors")
    
    save_results(acteptors_results_id3, "id3", "acteptors")
    save_results(donors_results_id3, "id3", "donors")  

def crossing_validation(examples: [Example], k: int, tree_builder):
    random.shuffle(examples)
    remaining_examples = len(examples)
    testing_set_size = int(remaining_examples/k)
    
    accuracy = 0
    iteration = 0

    while remaining_examples - testing_set_size >= testing_set_size:
        testing_set_start_index = remaining_examples-testing_set_size
        testing_set = examples[testing_set_start_index:remaining_examples]
        training_set = examples[:testing_set_start_index] + examples[remaining_examples:]
        remaining_examples = testing_set_start_index
        

        print("Testing set size: " + str(len(testing_set)))
        print("Training set size: " + str(len(training_set)))
        tree = tree_builder(training_set)
        print("Created tree:")
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
    print("Tree answers matching: " + str(matching/len(results)) + "\n")
    return matching/len(results)

def save_results(results, tree_type: str, set_type: str):
    if tree_type == "c45":
        tree_type_string = "C4.5"
    else:
        tree_type_string = "ID3"
    for result in results:
        print("Average " +tree_type_string +" acteptors matching for a number of subsets of  " + str(result[0]) + ": " + str(result[1]))
    print()

    file_name = "results/" + tree_type + "_" +set_type +"_crossing_validation.json"
    with open(file_name, "w") as file:
        json.dump(results, file)