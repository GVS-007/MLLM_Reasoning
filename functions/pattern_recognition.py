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
    
def pattern_recognition_questions(question_items, object_type):
    qa_pairs = []

    # 1. Sequence Recognition:
    # For simplicity, we're assuming the pattern is doubling of counts.
    items_sorted_by_count = sorted(question_items.items(), key=lambda x: x[1])

    if len(items_sorted_by_count) >= 2:
        is_doubling_pattern = all(items_sorted_by_count[i][1] == 2 * items_sorted_by_count[i-1][1] for i in range(1, len(items_sorted_by_count)))

        if is_doubling_pattern:
            next_count = 2 * items_sorted_by_count[-1][1]
            question_seq = f"Given the sequence of items, what is the likely count of the next item to be added in the image?"
            qa_pairs.append({
                "question": question_seq,
                "answer": f"There would likely be {int(next_count)} of the next item based on the pattern.",
                "question_type": "pattern_recognition",
                "answer_type": "string",
                "category_type": object_type,
                "source_function": "pattern_recognition_questions"
            })
            
    if len(items_sorted_by_count) >= 3:
        differences = [items_sorted_by_count[i][1] - items_sorted_by_count[i-1][1] for i in range(1, len(items_sorted_by_count))]
        is_ap = all(diff == differences[0] for diff in differences)

        if is_ap:
            next_item_count = items_sorted_by_count[-1][1] + differences[0]
            question_ap = f"Given the sequence of items, what is the likely count of the next item to be added in the image?"
            qa_pairs.append({
                "question": question_ap,
                "answer": f"There would likely be {int(next_item_count)} of the next item based on the Arithmetic Progression pattern.",
                "question_type": "ap_recognition",
                "answer_type": "string",
                "category_type": object_type,
                "source_function": "pattern_recognition_questions"
            })

    # 3. Geometric Progression (GP) Recognition:
    # Check if the sequence is a geometric progression.
    if len(items_sorted_by_count) >= 2:
        ratios = [items_sorted_by_count[i][1] / items_sorted_by_count[i-1][1] for i in range(1, len(items_sorted_by_count))]
        is_gp = all(ratio == ratios[0] for ratio in ratios)

        if is_gp:
            next_item_count = items_sorted_by_count[-1][1] * ratios[0]
            question_gp = f"Given the sequence of items, what is the likely count of the next item to be added in the image?"
            qa_pairs.append({
                "question": question_gp,
                "answer": f"There would likely be {int(next_item_count)} of the next item based on the Geometric Progression pattern.",
                "question_type": "gp_recognition",
                "answer_type": "string",
                "category_type": object_type,
                "source_function": "pattern_recognition_questions"
            })
            
    # 4. Fibonacci Series Recognition:
    # Check if the sequence is a Fibonacci series.
    if len(items_sorted_by_count) >= 3:
        is_fibonacci = all(items_sorted_by_count[i][1] == items_sorted_by_count[i-1][1] + items_sorted_by_count[i-2][1] for i in range(2, len(items_sorted_by_count)))

        if is_fibonacci:
            next_item_count = items_sorted_by_count[-1][1] + items_sorted_by_count[-2][1]
            question_fib = f"Given the sequence of items, what is the likely count of the next item to be added in the image?"
            qa_pairs.append({
                "question": question_fib,
                "answer": f"There would likely be {int(next_item_count)} of the next item based on the Fibonacci pattern.",
                "question_type": "fibonacci_recognition",
                "answer_type": "string",
                "category_type": object_type,
                "source_function": "pattern_recognition_questions"
            })


    # 5. Odd One Out:
    # We'll check if there's any item that belongs to a different category than the others.
    categories = get_category(question_items.keys())
    category_counts = {category: sum(1 for item in question_items if item in object_dictionary[category]["items"]) for category in categories}

    # Check if only one item belongs to a different category
    single_out_category = [category for category, count in category_counts.items() if count == 1]
    majority_category = [category for category, count in category_counts.items() if count > 1]

    if len(single_out_category) == 1 and len(majority_category) == 1:
        odd_item = next(item for item in question_items if item in object_dictionary[single_out_category[0]]["items"])
        question_odd = f"Pick the odd one out in the image."
        qa_pairs.append({
            "question": question_odd,
            "answer": odd_item,
            "question_type": "pattern_recognition",
            "answer_type": "string",
            "category_type": object_type,
            "source_function": "pattern_recognition_questions"
        })

    return qa_pairs
