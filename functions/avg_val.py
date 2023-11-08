import numpy as np
import itertools
import math
import random
import numpy as np

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


def average_point_value(question_items, object_type):
    np.random.seed(42)
    qa_pairs = []
    
    # Assign random points to each object type
    point_values = {key: np.random.randint(1, 6) for key in question_items.keys()}

    # Compute total points and count for each super category
    total_points = {category: 0 for category in object_dictionary.keys()}
    total_counts = {category: 0 for category in object_dictionary.keys()}
    for item, count in question_items.items():
        for category, details in object_dictionary.items():
            if item in details["items"]:
                total_points[category] += point_values[item] * count
                total_counts[category] += count
                break
    
    # Generate questions
    for super_category, details in object_dictionary.items():
        relevant_items = [item for item in details["items"] if item in question_items.keys()]
        if not relevant_items:
            continue
        
        question_parts = [f"{item} counts as {point_values[item]} points" for item in relevant_items]
        
        if len(question_parts) == 1:
            continue
            question = f"If each {question_parts[0]}, what's the average point value of the {super_category} in the image?"
        elif(len(question_parts) > 1):
            question = f"If each " + ', '.join(question_parts[:-1]) + f" and {question_parts[-1]}, what's the average point value of the {super_category} in the image?"
        
            average_value = total_points[super_category] / total_counts[super_category] if total_counts[super_category] != 0 else 0
            
            qa_pairs.append({
                "question": question,
                "answer": average_value,
                "question_type": "average_point_value",
                "answer_type": "float",
                "category_type": object_type,
                "operation": "average",
                "source_function": "average_point_value"
            })

    return qa_pairs
