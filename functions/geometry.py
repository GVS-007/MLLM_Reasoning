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

}

object_dictionary = {
    "fruit": {
        "items": [
            "apple",
            "orange",
            # "banana",
            # "strawberry",
            # "grape",
        ],
        "range": [1]
    },

    "vegetable": {
        "items": [
            "carrot",
            "broccoli",
            # "tomato",
            # "potato",
            # "cabbage"
        ],
        "range": [1]
    },

    "animal":{
        "items": [
            "dog",
            "cat",
            # "elephant",
            # "giraffe",
            # "dolphin"
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

def generate_shape_questions(question_items, object_type):
    qa_pairs = []

    # Define a mapping of shape names to their corresponding vertices and edges
    shape_mapping = {
        "triangle": {"vertices": 3, "edges": 3},
        "square": {"vertices": 4, "edges": 4},
        "pentagon": {"vertices": 5, "edges": 5},
        "hexagon": {"vertices": 6, "edges": 6},
        "octagon": {"vertices": 8, "edges": 8},
    }

    # Extract the shape names and their counts from the provided data    
    shapes_counts = {shape.lower(): count for shape, count in question_items.items()}

    # Sampled items to check for categories
    sampled_items = list(shapes_counts.keys())

    # Extract the names of objects belonging to the "geometry" category
    categories = get_category(sampled_items)

    # Check if any of the objects in the data belong to the "geometry" category
    has_geometry_objects = "geometry" in categories

    if has_geometry_objects:
        # Question 1: What are the different shapes present?
        shapes_present = [shape for shape in shapes_counts.keys() if shape in shape_mapping]
        question_1 = "If there are any geometric shapes in the image, What shapes are present?"
        answer_1 = ", ".join(shapes_present)
        qa_pairs.append({
            "question": question_1,
            "answer": answer_1,
            "question_type": "geometry",
            "answer_type": "string",
            "object_type": object_type,  # Add object_type here
            "source_function": "generate_shape_questions"
        })

        # Question 2: What are the total number of vertices present?
        total_vertices = sum(shape_mapping[shape]["vertices"] * count for shape, count in shapes_counts.items() if shape in shape_mapping)
        question_2 = "What are the total number of vertices present in all the geometric shapes in the image?"
        answer_2 = total_vertices
        qa_pairs.append({
            "question": question_2,
            "answer": answer_2,
            "question_type": "geometry",
            "answer_type": "int",
            "object_type": object_type,  # Add object_type here
            "source_function": "generate_shape_questions"
        })

        # Question 3: What are the total number of edges present?
        total_edges = sum(shape_mapping[shape]["edges"] * count for shape, count in shapes_counts.items() if shape in shape_mapping)
        question_3 = "What is the total number of edges present in all the geometric shapes in the image?"
        answer_3 = total_edges
        qa_pairs.append({
            "question": question_3,
            "answer": answer_3,
            "question_type": "geometry",
            "answer_type": "int",
            "object_type": object_type,  # Add object_type here
            "source_function": "generate_shape_questions"
        })
        
        for shape in shape_mapping.keys():
            shape_count = shapes_counts.get(shape, 0)
            if shape_count > 0:
                question_shape = f"If there are any {shape}s in the image, how many are there?"
                answer_shape = shape_count
                qa_pairs.append({
                    "question": question_shape,
                    "answer": answer_shape,
                    "question_type": "shape_count",
                    "answer_type": "int",
                    "object_type": object_type,  # Use the shape as object_type
                    "source_function": "generate_shape_questions"
                })
                
    return qa_pairs
