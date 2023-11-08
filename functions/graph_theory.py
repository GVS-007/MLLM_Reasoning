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
    
    

def generate_graph_theory_questions(question_items, object_type):
    qa_pairs = []

    # Extracting all items and categories present in the image
    items_present = list(question_items.keys())
    categories_present = get_category(items_present)

    # Connectivity question template
    connectivity_template = "If each {} connects to two distinct {}, and there are more {} than {}, how many {} do you need to add to ensure all connections in the image?"
    for item1, item2 in itertools.combinations(items_present, 2):
        extra_needed = max(0, (2 * question_items[item1] - question_items[item2]))
        question = connectivity_template.format(item1, item2, item1, item2, item2)
        qa_pairs.append({
            "question": question,
            "answer": extra_needed,
            "question_type": "graph theory - connectivity",
            "answer_type": "int",
            "category_type": object_type,
            "source_function": "generate_graph_theory_questions"
        })

    # Cycles question template
    cycles_template = "Given that each {} connects to a {}, and each {} connects back to a different {}, how many cycles are formed in the image?"
    for item1, item2 in itertools.combinations(items_present, 2):
        cycles = min(question_items[item1], question_items[item2])
        question = cycles_template.format(item1, item2, item2, item1)
        qa_pairs.append({
            "question": question,
            "answer": cycles,
            "question_type": "graph theory - cycles",
            "answer_type": "int",
            "category_type": object_type,
            "source_function": "generate_graph_theory_questions"
        })

    # Bipartite Graphs question template
    bipartite_template = "If every {} in the image is connected to a {}, and there are some connections between {}, can the relationship still represent a bipartite graph?"
    for item1, item2 in itertools.combinations(items_present, 2):
        question = bipartite_template.format(item1, item2, item2)
        answer = "No" if item1 == item2 else "Yes"  # If the items are the same, then it can't be a bipartite graph
        qa_pairs.append({
            "question": question,
            "answer": answer,
            "question_type": "graph theory - bipartite",
            "answer_type": "boolean",
            "category_type": object_type,
            "source_function": "generate_graph_theory_questions"
        })

    return qa_pairs
