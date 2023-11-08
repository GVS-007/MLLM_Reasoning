import numpy as np
import itertools
import math
from math import comb
import random
import numpy as np
import itertools
np.random.seed(42)


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
    
    

def multiple_operations_two_ops(question_items, object_type):
    qa_pairs = []
    operations = ["add", "takes away", "double", "triple"]
    question_templates = [
        "In the image, if a person {op_1}s {item_1_name} and {op_2}s {item_2_name}, how many total {query_item_name} will be there in the image?",
        "In the image, if a person {op_1}s {count_1} {item_1_name} and {op_2}s {count_2} {item_2_name}, how many total {query_item_name} will be there in the image?",
        "In the image, if a person {op_1}s {item_1_name} and {op_2}s {count_2} {item_2_name}, how many total {query_item_name} will be there in the image?",
        "In the image, if a person {op_1}s {count_1} {item_1_name} and {op_2}s {item_2_name}, how many total {query_item_name} will be there in the image?",
        
        "In the image, if a person {op_1}s {item_1_name} and {op_2}s {item_2_name}, how many total {super_category_name} will be there in the image?",
        "In the image, if a person {op_1}s {count_1} {item_1_name} and {op_2}s {count_2} {item_2_name}, how many total {super_category_name} will be there in the image?",
        "In the image, if a person {op_1}s {item_1_name} and {op_2}s {count_2} {item_2_name}, how many total {super_category_name} will be there in the image?",
        "In the image, if a person {op_1}s {count_1} {item_1_name} and {op_2}s {item_2_name}, how many total {super_category_name} will be there in the image?"
    ]

    # selected_objects = random.sample(list(question_items.keys()), 2)

    for object_1, object_2 in itertools.combinations(list(question_items.keys()), 2):
        print(object_1, object_2)
        for count_1 in range(1, 2):  # Operation on first object
            for count_2 in range(1, 2):  # Operation on second object
                for op_1 in operations:
                    for op_2 in operations:
                        # Check for valid operations
                        if (op_1 == "takes away" and question_items[object_1] - count_1 < 0) or \
                        (op_2 == "takes away" and question_items[object_2] - count_2 < 0):
                            continue

                        for template in question_templates:
                            if (op_1 in ["double", "triple"] and "{count_1}" in template) or \
                            (op_2 in ["double", "triple"] and "{count_2}" in template) or\
                                (op_1 in ["add", "takes away"] and "{count_1}" not in template) or \
                                    (op_2 in ["add", "takes away"] and "{count_2}" not in template):
                                continue
                            
                            if "super_category_name" in template:
                                super_category = None
                                for category, details in object_dictionary.items():
                                    if object_1 in details["items"]:
                                        super_category = category
                                        break
                                if super_category:
                                    super_category_name = plural_dictionary[super_category]
                                    question = template.format(op_1=op_1, count_1=count_1, item_1_name=object_1 if count_1 == 1 else plural_dictionary[object_1], op_2=op_2, count_2=count_2, item_2_name=object_2 if count_2 == 1 else plural_dictionary[object_2], super_category_name=super_category_name)
                                    answer = sum([question_items.get(item, 0) for item in object_dictionary[super_category]["items"]])
                                    
                                    if op_1 == "add" and object_1 in object_dictionary[super_category]["items"]:
                                        answer += count_1
                                    elif op_1 == "takes away" and object_1 in object_dictionary[super_category]["items"]:
                                        answer -= count_1
                                    elif op_1 == "double" and object_1 in object_dictionary[super_category]["items"]:
                                        answer += question_items[object_1]
                                    elif op_1 == "triple" and object_1 in object_dictionary[super_category]["items"]:
                                        answer += 2 * question_items[object_1]

                                    if op_2 == "add" and object_2 in object_dictionary[super_category]["items"]:
                                        answer += count_2
                                    elif op_2 == "takes away" and object_2 in object_dictionary[super_category]["items"]:
                                        answer -= count_2
                                    elif op_2 == "double" and object_2 in object_dictionary[super_category]["items"]:
                                        answer += question_items[object_2]
                                    elif op_2 == "triple" and object_2 in object_dictionary[super_category]["items"]:
                                        answer += 2 * question_items[object_2]

                            else:
                                queried_object = object_1
                                query_item_name = plural_dictionary[queried_object]
                                question = template.format(op_1=op_1, count_1=count_1, item_1_name=object_1 if count_1 == 1 else plural_dictionary[object_1], op_2=op_2, count_2=count_2, item_2_name=object_2 if count_2 == 1 else plural_dictionary[object_2], query_item_name=query_item_name)
                                answer = question_items[queried_object]
                                
                                if op_1 == "add" and queried_object == object_1:
                                    answer += count_1
                                elif op_1 == "takes away" and queried_object == object_1:
                                    answer -= count_1
                                elif op_1 == "double"and queried_object == object_1:
                                    answer += question_items[object_1]
                                elif op_1 == "triple" and queried_object == object_1:
                                    answer += 2 * question_items[object_1]

                                if op_2 == "add" and queried_object == object_2:
                                    answer += count_2
                                elif op_2 == "takes away" and queried_object == object_2:
                                    answer -= count_2
                                elif op_2 == "double" and queried_object == object_2:
                                        answer += question_items[object_2]
                                elif op_2 == "triple" and queried_object == object_2:
                                        answer += 2 * question_items[object_2]

                            qa_pairs.append({
                                "question": question,
                                "answer": answer,
                                "question_type": "multiple_operations_two_ops",
                                "answer_type": "int",
                                "category_type": object_type,
                                "operation": op_1 + "_" + op_2,
                                "source_function": "multiple_operations_two_ops"
                            })
    
    return qa_pairs

# # Testing with the given scenario
# test_items = {'apple': 2, 'orange': 3, 'dog': 1}
# result = multiple_operations_two_ops(test_items, "fruit")
# for qa_pair in result:
#     print(qa_pair)
