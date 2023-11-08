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
    
    


def comparison_questions(question_items, object_type):
    qa_pairs = []

    # 1. Direct comparison between two items
    items_list = list(question_items.keys())
    for i, item_i in enumerate(items_list):
        for j, item_j in enumerate(items_list[i+1:]):  # Ensures each pair is considered only once
            if question_items[item_i] > question_items[item_j]:
                answer = item_i
            elif question_items[item_i] < question_items[item_j]:
                answer = item_j
            else:
                answer = "both have the same count"

            question_comp = f"Are there more {item_i}s or {item_j}s in the image?"
            qa_pairs.append({
                "question": question_comp,
                "answer": answer,
                "question_type": "comparison",
                "answer_type": "string",
                "category_type": object_type,
                "source_function": "generate_comparison_questions"
            })

    # 2. Item with the least count in a category
    for category in get_category(question_items.keys()):
        items = object_dictionary[category]["items"]
        counts = [(item, question_items.get(item, 0)) for item in items if item in question_items]
        counts.sort(key=lambda x: x[1])
        if counts:
            least_item = counts[0][0]
            question_least = f"Which {category} has the least count in the image?"
            qa_pairs.append({
                "question": question_least,
                "answer": least_item,
                "question_type": "comparison",
                "answer_type": "string",
                "category_type": object_type,
                "source_function": "generate_comparison_questions"
            })

    # 3. Compare counts between categories
    categories_list = list(get_category(question_items.keys()))
    for i, category_i in enumerate(categories_list):
        for j, category_j in enumerate(categories_list[i+1:]):  # Ensures each pair is considered only once
            count_i = sum([question_items.get(item, 0) for item in object_dictionary[category_i]["items"]])
            count_j = sum([question_items.get(item, 0) for item in object_dictionary[category_j]["items"]])
            if count_i > count_j:
                answer = category_i
            elif count_i < count_j:
                answer = category_j
            else:
                answer = "both have the same count"

            question_comp = f"Are there more {plural_dictionary[category_i]} or {plural_dictionary[category_j]} in the image?"
            qa_pairs.append({
                "question": question_comp,
                "answer": answer,
                "question_type": "comparison",
                "answer_type": "string",
                "category_type": object_type,
                "source_function": "generate_comparison_questions"
            })

    return qa_pairs
