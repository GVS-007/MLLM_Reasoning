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
    
    


def probability_questions(question_items, object_type):
    qa_pairs = []

    # Total items
    total_items = sum(question_items.values())

    # 1. Probability of picking a specific object from all objects
    for item, count in question_items.items():
        prob = count / total_items
        question_prob = f"What's the probability of picking an {item} from all objects in the image?"
        qa_pairs.append({
            "question": question_prob,
            "answer": prob,
            "question_type": "probability",
            "answer_type": "float",
            "category_type": object_type,
            "source_function": "generate_advanced_probability_questions"
        })

    # 2. Probability of picking a specific object after removing another object
    for item_i in question_items.keys():
        for item_j in question_items.keys():
            if item_i != item_j:
                prob = question_items[item_i] / (total_items - 1)
                question_prob = f"What's the probability of picking an {item_i} after taking away one {item_j} from all objects in the image?"
                qa_pairs.append({
                    "question": question_prob,
                    "answer": prob,
                    "question_type": "probability",
                    "answer_type": "float",
                    "category_type": object_type,
                    "source_function": "generate_advanced_probability_questions"
                })

    # 3. Given that an object is of a specific category, probability it's of a specific type
    def get_article(item):
        return "an" if item[0].lower() in "aeiou" else "a"
    
    for category in get_category(question_items.keys()):
        for item in object_dictionary[category]["items"]:
            if question_items.get(item, 0) > 0:
                prob = question_items[item] / sum([question_items.get(item, 0) for item in object_dictionary[category]["items"]])
                article = get_article(item)
                question_prob = f"Given that the picked object is a {category}, what's the probability it's {article} {item} in the image?"
                qa_pairs.append({
                    "question": question_prob,
                    "answer": prob,
                    "question_type": "probability",
                    "answer_type": "float",
                    "category_type": object_type,
                    "source_function": "generate_advanced_probability_questions"
                })

   
    return qa_pairs

