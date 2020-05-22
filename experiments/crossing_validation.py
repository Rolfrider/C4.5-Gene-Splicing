from algorithm.data_struct import *
from algorithm.tree import build_tree, c45
import json
import random
import matplotlib.pyplot as plt

def test_crossing_validation(acteptors_examples: [Example], donors_examples: [Example]):
    k = 10
    iteration = 100
    acteptors_results = []
    donors_results = []
    acteptors_results_id3 = []
    donors_results_id3 = []
    
    a_result = 0
    d_result = 0
    a_result_id3 = 0
    d_result_id3 = 0
    for i in range(0, iteration):
        a_result += crossing_validation(acteptors_examples, k)
        d_result += crossing_validation(donors_examples, k)
        a_result_id3 += crossing_validation(acteptors_examples, k, "id3")
        d_result_id3 += crossing_validation(donors_examples, k, "id3")
        
    acteptors_results.append(((str)(k), a_result/iteration))
    donors_results.append(((str)(k), d_result/iteration))
    acteptors_results_id3.append(((str)(k), a_result_id3/iteration))
    donors_results_id3.append(((str)(k), d_result_id3/iteration))
    
    save_results(acteptors_results, "c45", "acteptors")
    save_results(donors_results, "c45", "donors")
    #file_name = "results/c45_aceptors_crossing_validation.json"
    #with open(file_name, "w") as file:
    #    json.dump(acteptors_results, file)
    #file_name = "results/c45_donors_crossing_validation.json"
    #with open(file_name, "w") as file:
    #    json.dump(donors_results, file)
    
    #for result in acteptors_results:
    #    print("Average C4.5 acteptors matching for a number of subsets of  " + str(result[0]) + ": " + str(result[1]))
    #print()
    #for result in donors_results:
    #    print("Average C4.5 donors matching for a number of subsets of " + str(result[0]) + ": " + str(result[1]))
    #print()
    
    save_results(acteptors_results_id3, "id3", "acteptors")
    save_results(donors_results_id3, "id3", "donors")
    #file_name = "results/id3_aceptors_crossing_validation.json"
    #with open(file_name, "w") as file:
    #    json.dump(acteptors_results_id3, file)
    #file_name = "results/id3_donors_crossing_validation.json"
    #with open(file_name, "w") as file:
    #    json.dump(donors_results_id3, file)
    
    #for result in acteptors_results_id3:
    #    print("Average id3 acteptors matching for a number of subsets of " + str(result[0]) + ": " + str(result[1]))
    #print()
    #for result in donors_results_id3:
    #    print("Average id3 donors matching for a number of subsets of " + str(result[0]) + ": " + str(result[1]))

    save_plot("acteptors_matching", acteptors_results, acteptors_results_id3)
    save_plot("donors_matching", donors_results, donors_results_id3)
    

def crossing_validation(examples: [Example], k: int, tree_type = "C4.5"):
    size = len(examples)
    random.shuffle(examples)
    testing_set_size = (int)(size/k)
    remaining_examples = size
    accuracy = 0
    iteration = 0

    while remaining_examples - testing_set_size >= testing_set_size:
        testing_set_start_index = remaining_examples-testing_set_size
        testing_set = examples[testing_set_start_index:remaining_examples]
        training_set = examples[:testing_set_start_index] + examples[remaining_examples:]
        remaining_examples = testing_set_start_index
        

        print("Testing set size: " + str(len(testing_set)))
        print("Training set size: " + str(len(training_set)))
        tree = build_tree(training_set)
        if tree_type == "C4.5":
            tree = c45(tree)
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

def save_plot(title: str, results_c45, results_id3):
    fig = plt.figure()
    #for k, result in results_c45:
    label = "test_c45"
    plt.plot([x[0] for x in results_c45], [x[1] for x in results_c45], label=label)

    #for k, result in results_id3:
    label = "test_id3"
    plt.plot([x[0] for x in results_id3], [x[1] for x in results_id3], label=label)

    plt.title(title)
    plt.xlabel("Iterations")
    plt.ylabel("Score")
    plt.legend(loc='best')
    fig.savefig("results/" + title + ".pdf")

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