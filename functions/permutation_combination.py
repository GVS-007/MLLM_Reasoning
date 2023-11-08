import numpy as np
import itertools
import math
from math import comb
import random
import numpy as np
import itertools


plural_dictionary = {
    "fruit": "fruits",
    "apple": "apples",
    "orange": "oranges",
    "banana": "bananas",
    "strawberry": "strawberries",
    "grape": "grapes",

    "vegetable": "vegetables",
    "carrot": "carrots",
    "broccoli": "broccoli",
    "tomato": "tomatoes",
    "potato": "potatoes",
    "cabbage": "cabbages",
    
    "animal": "animals",
    "dog": "dogs",
    "cat": "cats",
    "elephant": "elephants",
    "giraffe": "giraffes",
    "dolphin": "dolphins",

}

object_dictionary = {
    "fruit": {
        "items": [
            "apple",
            "orange",
            "banana",
            "strawberry",
            "grape",
        ],
        "range": [1, 5]
    },

    "vegetable": {
        "items": [
            "carrot",
            "broccoli",
            "tomato",
            "potato",
            "cabbage"
        ],
        "range": [1, 3]
    },

    "animal":{
        "items": [
            "dog",
            "cat",
            "elephant",
            "giraffe",
            "dolphin"
        ],
        "range": [1, 3]
    }
}


def get_category(sampled_items):
    categories = set()
    for item in sampled_items:
        for category, details in object_dictionary.items():
            if item in details["items"]:
                categories.add(category)
                break
    return categories


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
    
   

def permutations(question_items, object_type):
    qa_pairs = []

    # Calculating total items
    total_items = sum(question_items.values())
    
    categories = set()
    for item in question_items.keys():
        for category, details in object_dictionary.items():
            if item in details["items"]:
                categories.add(category)
                break

    # Permutations
    permutations_denom = 1
    for item_count in question_items.values():
        permutations_denom *= factorial(item_count)

    permutations_total = factorial(total_items) / permutations_denom

    
    question_permutations = f"In the image, considering repetitions, how many sequences can you arrange all the objects in?"
    qa_pairs.append({
        "question": question_permutations,
        "answer": permutations_total,
        "question_type": "permutations",
        "answer_type": "int",
        "category_type": object_type,
        "source_function": "permutations_combinations"
    })
    
    for category in categories:
        question_permutations = f"In the image, considering repetitions, how many sequences can you arrange all {plural_dictionary[category]} in?"
        fact_num = factorial(sum([question_items.get(item, 0) for item in object_dictionary[category]["items"]]))
        fact_denom = 1
        for item_count in [question_items.get(item, 0) for item in object_dictionary[category]["items"]]:
            fact_denom *= factorial(item_count)
        permutations_total = fact_num/fact_denom
            
        
        qa_pairs.append({
            "question": question_permutations,
            "answer": permutations_total,
            "question_type": "permutations",
            "answer_type": "int",
            "category_type": object_type,
            "source_function": "permutations_combinations",
        })
    
    # # Combinations for various group sizes
    # for group_size in range(1, total_items + 1):
    #     combinations_total = factorial(total_items) / (factorial(group_size) * factorial(total_items - group_size))

    #     question_combinations = f"From the image, how can you select a group of {group_size} {object_type}?"
    #     qa_pairs.append({
    #         "question": question_combinations,
    #         "answer": combinations_total,
    #         "question_type": "combinations",
    #         "answer_type": "int",
    #         "category_type": object_type,
    #         "source_function": "permutations_combinations"
    #     })

    return qa_pairs


def comb(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def combinations(question_items, object_type):
    qa_pairs = []

    # Global combinations
    total_items = sum(question_items.values())
    for r in range(2, total_items+1):
        combinations_total = comb(total_items, r)
        question_combinations = f"How many ways can you select {r} objects from the image?"
        qa_pairs.append({
            "question": question_combinations,
            "answer": combinations_total,
            "question_type": "combinations",
            "answer_type": "int",
            "category_type": object_type,
            "source_function": "generate_combination_questions"
        })

    # For each category
    
    categories = get_category(question_items.keys())
    
    
    for category in categories:
        total_items_in_category = sum([question_items.get(item, 0) for item in object_dictionary[category]["items"]])

        for r in range(2, total_items_in_category+1):
            combinations_total = comb(total_items_in_category, r)
            question_combinations = f"How many ways can you select {r} {plural_dictionary[category]} from the image?"
            qa_pairs.append({
                "question": question_combinations,
                "answer": combinations_total,
                "question_type": "combinations",
                "answer_type": "int",
                "category_type": object_type,
                "source_function": "generate_combination_questions"
            })

        # Questions for each specific item pairing in the category
        for i, item_i in enumerate(question_items.keys()):
            for j, item_j in enumerate(list(question_items.keys())[i+1:]):
                if question_items.get(item_i, 0) >= 1 and question_items.get(item_j, 0) >= 1:
                    combinations_total = question_items[item_i] * question_items[item_j]
                    question_combinations = f"In how many ways can you select 1 {item_i} and 1 {item_j} from the image?"
                    qa_pairs.append({
                        "question": question_combinations,
                        "answer": combinations_total,
                        "question_type": "combinations",
                        "answer_type": "int",
                        "category_type": object_type,
                        "source_function": "generate_combination_questions"
                    })

    return qa_pairs

