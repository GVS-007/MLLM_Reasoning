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
    
    "clock" : "clocks",
    "clock 1" : "clocks",
    "clock 2" : "clocks",
    "clock 3" : "clocks",
    "clock 4" : "clocks",
    "clock 5" : "clocks",
    "clock 6" : "clocks",
    "clock 7" : "clocks",
    "clock 8" : "clocks",
    "clock 9" : "clocks",
    "clock 10" : "clocks",
    "clock 11" : "clocks",
    "clock 12" : "clocks",
    
    "geometry": "geometries",
    "triangle": "triangles",
    "square": "squares",
    "pentagon": "pentagons",
    "hexagon": "hexagons",
    "octagon": "octagons",

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
    
    

def number_theory_questions(question_items, object_type):
    qa_pairs = []

    # Extracting all items and categories present in the image
    items_present = list(question_items.keys())
    categories_present = get_category(items_present)

    # Divisibility question templates
    divisibility_templates = [
        "Is the sum of the total number of {} and {} in the image divisible by the number of {}?",
        "Is the number of {} in the image divisible by the total number of {}?"
    ]

    # Factors question templates
    factors_templates = [
        "Is the number of {} a factor of the total number of {} in the image?",
        "Is the total number of {} a factor of the total number of {} in the image?"
    ]

    # Populating divisibility questions
    for item1, item2, item3 in itertools.combinations(items_present, 3):
        question = divisibility_templates[0].format(item1, item2, item3)
        total = question_items[item1] + question_items[item2]
        answer = "Yes" if total % question_items[item3] == 0 else "No"
        qa_pairs.append({
            "question": question,
            "answer": answer,
            "question_type": "number theory - divisibility",
            "answer_type": "boolean",
            "category_type": object_type,
            "source_function": "generate_number_theory_questions"
        })
    
    for item, category in itertools.product(items_present, categories_present):
        question = divisibility_templates[1].format(item, category)
        total_category_count = sum([question_items.get(i, 0) for i in object_dictionary[category]["items"]])
        answer = "Yes" if total_category_count % question_items[item] == 0 else "No"
        qa_pairs.append({
            "question": question,
            "answer": answer,
            "question_type": "number theory - divisibility",
            "answer_type": "boolean",
            "category_type": object_type,
            "source_function": "generate_number_theory_questions"
        })

    # Populating factors questions
    for item, category in itertools.product(items_present, categories_present):
        question = factors_templates[0].format(plural_dictionary[item], plural_dictionary[category])
        total_category_count = sum([question_items.get(i, 0) for i in object_dictionary[category]["items"]])
        answer = "Yes" if total_category_count % question_items[item] == 0 else "No"
        qa_pairs.append({
            "question": question,
            "answer": answer,
            "question_type": "number theory - factors",
            "answer_type": "boolean",
            "category_type": object_type,
            "source_function": "generate_number_theory_questions"
        })

    for category1, category2 in itertools.combinations(categories_present, 2):
        question = factors_templates[1].format(plural_dictionary[category1], plural_dictionary[category2])
        total_category1_count = sum([question_items.get(i, 0) for i in object_dictionary[category1]["items"]])
        total_category2_count = sum([question_items.get(i, 0) for i in object_dictionary[category2]["items"]])
        answer = "Yes" if total_category2_count % total_category1_count == 0 else "No"
        qa_pairs.append({
            "question": question,
            "answer": answer,
            "question_type": "number theory - factors",
            "answer_type": "boolean",
            "category_type": object_type,
            "source_function": "generate_number_theory_questions"
        })

    return qa_pairs
