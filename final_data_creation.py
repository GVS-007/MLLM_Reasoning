import random
import itertools
import math
import json

from functions.counting import counting
from functions.multi_arithematic import multiple_operations_two_ops
from functions.single_arithematic import single_arithematic
from functions.avg_val import average_point_value
from functions.permutation_combination import permutations
from functions.permutation_combination import combinations
from functions.probability import probability_questions
from functions.comparisions import comparison_questions
from functions.logical import logical_questions
from functions.number_theory import number_theory_questions
from functions.graph_theory import generate_graph_theory_questions
from functions.pattern_recognition import pattern_recognition_questions
from functions.geometry import generate_shape_questions
from functions.clock import generate_clock_time_questions

from functions.algorithmic_reasoning import knapsack_questions
from functions.algorithmic_reasoning import greedy_questions
from functions.algorithmic_reasoning import sort_and_median_questions
from functions.algorithmic_reasoning import recursion_questions

from functions.temporal import temporal_questions
from functions.incomplete_question import incomplete_questions

from functions.spatial_reasoning import spatial_reasoning_questions

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
    
    "clock" : "clocks",

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


def determine_object_type(sampled_items):
    categories = set()
    for item in sampled_items:
        for category, details in object_dictionary.items():
            if item in details["items"]:
                categories.add(category)
                break
            
    if len(sampled_items) == 1:
        return "single_object"
    elif len(categories) == 1:
        return "intra_category"
    else:
        return "inter_category"

def test_create_QA():
    obj_to_return = []  
    question_item = {'clock 1': 1, 'square':2, 'orange': 4}
    object_key = determine_object_type([item for item in question_item.keys()])
    qa_pairs = []


    # qa_pairs += counting(question_item, object_key)
    # qa_pairs += multiple_operations_two_ops(question_item, object_key)
    # qa_pairs += single_arithematic(question_item, object_key)
    # qa_pairs += average_point_value(question_item, object_key)
    # qa_pairs += permutations(question_item, object_key)
    # qa_pairs += combinations(question_item, object_key)
    # qa_pairs += probability_questions(question_item, object_key)
    # qa_pairs += comparison_questions(question_item, object_key)
    # qa_pairs += logical_questions(question_item, object_key)
    # qa_pairs += number_theory_questions(question_item, object_key)
    # qa_pairs += generate_graph_theory_questions(question_item, object_key)
    # qa_pairs += pattern_recognition_questions(question_item, object_key)
    # qa_pairs += knapsack_questions(question_item, object_key)
    # qa_pairs += greedy_questions(question_item, object_key)
    # qa_pairs += sort_and_median_questions(question_item, object_key)
    # qa_pairs += recursion_questions(question_item, object_key)
    # qa_pairs += temporal_questions(question_item, object_key)
    # qa_pairs += incomplete_questions(question_item, object_key)
    # qa_pairs += spatial_reasoning_questions(question_item, object_key)
    # qa_pairs += generate_shape_questions(question_item, object_key)
    qa_pairs += generate_clock_time_questions(question_item, object_key)
    

    obj_to_return.append({
        "obj_json": question_item,
        "qa_pairs": qa_pairs,
    })
                    
    return obj_to_return

def create_QA():
    obj_to_return = []
    total_questions = 0
    
    # Flatten the items across all categories
    all_items = []
    for category, details in object_dictionary.items():
        all_items.extend(details["items"])
    
    items_range = [1, 5]  # A generic range for simplicity

    for L in range(1, len(all_items) + 1):      
        if L<=9:      
            for sampled_items in itertools.combinations(all_items, L):
                
                object_type = determine_object_type(sampled_items)
                number_of_objects = len(sampled_items)
                item_count_values = [i for i in range(items_range[0], items_range[1] + 1)]
                lists = [item_count_values] * number_of_objects

                for combination in itertools.product(*lists):
                    index = 0
                    qa_pairs = []
                    question_item = {}
                    for item in sampled_items:
                        item_count = combination[index]
                        question_item[item] = item_count
                        index += 1                    
                    
                    # Now, we generate questions for these combinations
                    qa_pairs += counting(question_item, object_type)
                    # qa_pairs += multiple_operations_two_ops_extended(number_of_objects, sampled_items, question_item)

                    obj_to_return.append({
                        "obj_json": question_item,
                        "qa_pairs": qa_pairs,
                    })
                    total_questions += len(qa_pairs)
                    
    print(f"Total questions: {total_questions}")
    return obj_to_return




if __name__ == "__main__":
    
    
    file_path = 'D:\MLMM_ASU\MLLM_Evaluation_Scale\display3.json'
    with open(file_path, 'w') as f:
        json.dump(test_create_QA(), f)