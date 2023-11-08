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
    

def single_arithematic(question_items, object_type):
    qa_pairs = []
    operations = ["adds", "takes away", "doubles", "triples"]
    person_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"]
    
    question_templates_adds = [
        "If a person adds {count_1} {item_1_name} to the image, how many total {query_item_name} will be there in the image?",
        "If a person adds {count_1} {item_1_name} to the image, how many total {super_category_name} will be there in the image?"
    ]
    question_templates_takes = [
        "If a person takes away {count_1} {item_1_name} from the image, how many total {query_item_name} will be there in the image?",
        "If a person takes away {count_1} {item_1_name} from the image, how many total {super_category_name} will be there in the image?"
    ]
    question_templates_dt = [
        "If a person {op_1} {item_1_name} in the image, how many total {query_item_name} will be there in the image?",
        "If a person {op_1} {item_1_name} in the image, how many total {super_category_name} will be there in the image?",
    ]
    

    for object_1 in question_items.keys():
        for count_1 in range(1, 2):  # Operation on the object
            for op_1 in operations:
                
                # Check for valid operations
                if op_1 == "takes away" and question_items[object_1] - count_1 < 0:
                    continue
                
                if op_1 == "adds":
                    question_templates = question_templates_adds
                if op_1 == "takes away":
                    question_templates = question_templates_takes
                if op_1 == "doubles" or op_1 == "triples":
                    question_templates = question_templates_dt
                

                for template in question_templates:
                    if (op_1 in ["doubles", "triples"] and "{count_1}" in template) or \
                    (op_1 in ["adds", "takes away"] and "{count_1}" not in template):
                        continue
                    
                    if "super_category_name" in template:
                        super_category = None
                        for category, details in object_dictionary.items():
                            if object_1 in details["items"]:
                                super_category = category
                                break
                        if super_category:
                            super_category_name = plural_dictionary[super_category]
                            # if object_1.split()[0] == "clock": object_1 = "clock"
                            print(object_1)
                            question = template.format(op_1=op_1, count_1=count_1, item_1_name=object_1 if count_1 == 1 else plural_dictionary[object_1], super_category_name=super_category_name)
                            answer = sum([question_items.get(item, 0) for item in object_dictionary[super_category]["items"]])
                            
                            if op_1 == "adds":
                                answer += count_1
                            elif op_1 == "takes away":
                                answer -= count_1
                            elif op_1 == "doubles":
                                answer += question_items[object_1]
                            elif op_1 == "triples":
                                answer += 2 * question_items[object_1]

                    else:
                        queried_object = object_1
                        query_item_name = plural_dictionary[queried_object]
                        if object_1.split()[0] == "clock": 
                            temp = object_1
                            object_1 = "clock"
                            
                        question = template.format(op_1=op_1, count_1=count_1, item_1_name=object_1 if count_1 == 1 else plural_dictionary[object_1], query_item_name=query_item_name)
                        answer = question_items[queried_object]
                        
                        if object_1 == "clock": 
                            object_1 = temp
                            
                        if op_1 == "adds":
                            answer += count_1
                        elif op_1 == "takes away":
                            answer -= count_1
                        elif op_1 == "doubles":
                            answer += question_items[object_1]
                        elif op_1 == "triples":
                            answer += 2 * question_items[object_1]

                    qa_pairs.append({
                        "question": question,
                        "answer": answer,
                        "question_type": "multiple_operations_single_op",
                        "answer_type": "int",
                        "category_type": object_type,
                        "operation": op_1,
                        "source_function": "multiple_operations_single_op"
                    })
    
    return qa_pairs
