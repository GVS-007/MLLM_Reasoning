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
    
    "geometry": "geometries",
    "triangle": "triangles",
    "square": "squares",
    "pentagon": "pentagons",
    "hexagon": "hexagons",
    "octagon": "octagons",
    
    "clock": "clocks",
    "clock 1": "clocks",
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
        "range": [1]
    },

    "vegetable": {
        "items": [
            "carrot",
            "broccoli",
            "tomato",
            "potato",
            "cabbage"
        ],
        "range": [1]
    },

    "animal":{
        "items": [
            "dog",
            "cat",
            "elephant",
            "giraffe",
            "dolphin"
        ],
        "range": [1]
    },
    
    "geometry": {
        "items": [
            "triangle",
            "square",
            "pentagon",
            "hexagon",
            "octagon"
    ],
    "range": [1]
    },
    
    "clock": {
        "items": [
            "clock 1",
            "clock 2",
            "clock 3",
            "clock 4",
            "clock 5",
            "clock 6",
            "clock 7",
            "clock 8",
            "clock 9",
            "clock 10",
            "clock 11",
            "clock 12"
    ],
    "range": [1]
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
    
    

def counting(question_items, object_type):
    qa_pairs = []
    
    # Questions about individual items
    for item, count in question_items.items():
        question = f"How many {plural_dictionary[item]} are there in the image?"
        qa_pairs.append({
            "question": question,
            "answer": count,
            "question_type": "counting",
            "answer_type": "int",
            "category_type": object_type,
            "operation": "addition",
            "source_function": "counting"
        })

    # Questions about super categories
    super_category_counts = {}
    for category, details in object_dictionary.items():
        super_category_counts[category] = sum([question_items.get(item, 0) for item in details["items"]])
    
    for super_category, count in super_category_counts.items():
        if count > 0:  # Only ask if there's at least one item from the super category
            question = f"How many {plural_dictionary[super_category]} are there in the image?"
            qa_pairs.append({
                "question": question,
                "answer": count,
                "question_type": "counting",
                "answer_type": "int",
                "category_type": object_type,
                "operation": "addition",
                "source_function": "counting"
            })
    
    return qa_pairs

