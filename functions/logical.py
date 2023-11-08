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
    
    

def logical_questions(question_items, object_type):
    qa_pairs = []

    items_present = list(question_items.keys())
    all_items = [item for category in object_dictionary for item in object_dictionary[category]["items"]]
    all_categories = list(object_dictionary.keys())

    # Question templates
    templates = {
        "AND": "Is it true that the image contains {} and {}?",
        "OR": "Is it true that the image contains either {} or {}?",
        "XOR": "Is it true that either {} is absent OR {} is present in the image, but not both?",
    }

    # Generating questions using templates and combinations
    for item1, item2 in itertools.combinations(all_items + all_categories, 2):
        for key, template in templates.items():
            question = template.format(item1, item2)

            if key == "AND":
                answer = "Yes" if item1 in items_present and item2 in items_present else "No"
            elif key == "OR":
                answer = "Yes" if item1 in items_present or item2 in items_present else "No"
            else:  # XOR
                condition = (item1 not in items_present) ^ (item2 in items_present)
                answer = "Yes" if condition else "No"

            qa_pairs.append({
                "question": question,
                "answer": answer,
                "question_type": "logical",
                "answer_type": "boolean",
                "category_type": object_type,
                "source_function": "generate_logical_questions_using_combinations"
            })

    # NOT Operator questions
    not_template = "Is it NOT true that {} is in the image?"
    for item in all_items + all_categories:
        question = not_template.format(item)
        answer = "Yes" if item not in items_present else "No"
        qa_pairs.append({
            "question": question,
            "answer": answer,
            "question_type": "logical",
            "answer_type": "boolean",
            "category_type": object_type,
            "source_function": "generate_logical_questions_using_combinations"
        })

    return qa_pairs
