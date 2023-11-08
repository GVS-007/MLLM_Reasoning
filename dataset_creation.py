import random
import itertools
import math


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

    "animals":{
        "items": [
            "dog",
            "cat",
            "elephant",
            "giraaffe",
            "dolphin"
        ],
        "range": [1, 3]
    }
}

# Conditional Questions - 1
# If n table is added, how many pieces of tables will remain?

def positive_add_items_to_object(number_of_objects, sampled_items, question_items):
    qa_pairs = []
    # Use placeholders in the template string
    question_templates = [
        "If a person adds {count} {item_name}, How many total {item_name} are there in the image?",
    ]
    
    #question_items = {"apple": 3, "orange": 2, "banana": 1, "strawberry": 4, "grape": 2}
    #sampled_items = ["apple", "orange", "banana", "strawberry", "grape"]
    #number_of_objects = 5
    
    for i in range(number_of_objects):
        sampled_question_template = question_templates[0]
        object_1 = sampled_items[i]
        
        for count in range(1, 4):
            # Determine the correct item name (singular or plural) based on count
            item_name = object_1 if count == 1 else plural_dictionary[object_1]
            
            # Format the question using the .format() method within the loop
            question = sampled_question_template.format(count=count, item_name=item_name)
            
            answer = question_items[sampled_items[i]] + count
            qa_pairs.append({
                "question": question,
                "answer": answer,
            })
            
    return qa_pairs

def negative_add_items_to_object_v2(number_of_objects, sampled_items, question_items):
    qa_pairs = []
    
    for i in range(number_of_objects):
        object_1 = sampled_items[i]  # The item being added
        
        for j in range(number_of_objects):
            if i != j:  # Ensure object_1 and object_2 are different
                object_2 = sampled_items[j]  # The item being asked about

                for count in range(1, 4):  # Adding 1, 2, or 3 items
                    question = f"If a person adds {count} {object_1 if count == 1 else plural_dictionary[object_1]}, How many total {plural_dictionary[object_2]} are there in the image?"
                    answer = question_items[object_2]
                    
                    qa_pairs.append({
                        "question": question,
                        "answer": answer,
                    })

    return qa_pairs


def positive_subtract_items_to_object(number_of_objects, sampled_items, question_items):
    qa_pairs = []

    for i in range(number_of_objects):
        object_1 = sampled_items[i]
        for count in range(1, 4):  # Taking away 1, 2, or 3 of object_1
            # Ensure that subtraction won't lead to negative counts
            if question_items[object_1] - count >= 0:
                question = f"If a person takes away {count} {object_1 if count == 1 else plural_dictionary[object_1]}, How many total {object_1 if count == 1 else plural_dictionary[object_1]} remain in the image?"
                answer = question_items[object_1] - count
                qa_pairs.append({
                    "question": question,
                    "answer": answer,
                })

    return qa_pairs



def negative_subtract_items_to_object(number_of_objects, sampled_items, question_items):
    qa_pairs = []

    for i in range(number_of_objects):
        object_1 = sampled_items[i]  # The item being taken away
        
        for j in range(number_of_objects):
            if i != j:  # Ensure object_1 and object_2 are different
                object_2 = sampled_items[j]  # The item being asked about

                for count in range(1, 4):  # Taking away 1, 2, or 3 of object_1
                    # Ensure that subtraction won't lead to negative counts for object_1
                    if question_items[object_1] - count >= 0:
                        question = f"If a person takes away {count} {object_1 if count == 1 else plural_dictionary[object_1]}, How many total {plural_dictionary[object_2]} remain in the image?"
                        answer = question_items[object_2]
                        qa_pairs.append({
                            "question": question,
                            "answer": answer,
                        })

    return qa_pairs





def complex_add_items_to_object(number_of_objects, sampled_items, question_items):
    qa_pairs = []

    # Generate questions for combinations of two distinct items
    for i in range(number_of_objects):
        for j in range(number_of_objects):
            # if i != j:  # Ensure we're looking at two different items
                object_1 = sampled_items[i]
                object_2 = sampled_items[j]
                
                for count_1 in range(1, 4):  # Adding 1, 2, or 3 of object_1
                    for count_2 in range(1, 4):  # Adding 1, 2, or 3 of object_2
                        
                        # Question about the total count of object_1
                        question_obj1 = f"If a person adds {count_1} {object_1 if count_1 == 1 else plural_dictionary[object_1]} and {count_2} {object_2 if count_2 == 1 else plural_dictionary[object_2]}, How many total {plural_dictionary[object_1]} are there in the image?"
                        answer_obj1 = question_items[object_1] + count_1
                        qa_pairs.append({
                            "question": question_obj1,
                            "answer": answer_obj1,
                        })

                        # Question about the total count of object_2
                        question_obj2 = f"If a person adds {count_1} {object_1 if count_1 == 1 else plural_dictionary[object_1]} and {count_2} {object_2 if count_2 == 1 else plural_dictionary[object_2]}, How many total {plural_dictionary[object_2]} are there in the image?"
                        answer_obj2 = question_items[object_2] + count_2
                        qa_pairs.append({
                            "question": question_obj2,
                            "answer": answer_obj2,
                        })

                        # Optional: Question about the total count of a distinct third item (uncomment if needed)
                        for k in range(number_of_objects):
                            if k != i and k != j:
                                object_3 = sampled_items[k]
                                question_obj3 = f"If a person adds {count_1} {object_1 if count_1 == 1 else plural_dictionary[object_1]} and {count_2} {object_2 if count_2 == 1 else plural_dictionary[object_2]}, How many total {plural_dictionary[object_3]} are there in the image?"
                                answer_obj3 = question_items[object_3]
                                qa_pairs.append({
                                    "question": question_obj3,
                                    "answer": answer_obj3,
                                })

    return qa_pairs



def complex_subtract_items_to_object(number_of_objects, sampled_items, question_items):
    qa_pairs = []

    # Generate questions for combinations of two distinct items
    for i in range(number_of_objects):
        for j in range(number_of_objects):
            if i != j:  # Ensure we're looking at two different items
                object_1 = sampled_items[i]
                object_2 = sampled_items[j]
                
                for count_1 in range(1, 4):  # Taking away 1, 2, or 3 of object_1
                    for count_2 in range(1, 4):  # Taking away 1, 2, or 3 of object_2
                        
                        # Ensure that subtraction won't lead to negative counts for either object
                        if question_items[object_1] - count_1 >= 0 and question_items[object_2] - count_2 >= 0:
                            
                            # Question about the total count of object_1
                            question_obj1 = f"If a person takes away {count_1} {object_1 if count_1 == 1 else plural_dictionary[object_1]} and {count_2} {object_2 if count_2 == 1 else plural_dictionary[object_2]}, How many total {object_1 if count_1 == 1 else plural_dictionary[object_1]} remain in the image?"
                            answer_obj1 = question_items[object_1] - count_1
                            qa_pairs.append({
                                "question": question_obj1,
                                "answer": answer_obj1,
                            })

                            # Question about the total count of object_2
                            question_obj2 = f"If a person takes away {count_1} {object_1 if count_1 == 1 else plural_dictionary[object_1]} and {count_2} {object_2 if count_2 == 1 else plural_dictionary[object_2]}, How many total {object_2 if count_2 == 1 else plural_dictionary[object_2]} remain in the image?"
                            answer_obj2 = question_items[object_2] - count_2
                            qa_pairs.append({
                                "question": question_obj2,
                                "answer": answer_obj2,
                            })

                            # Optional: Question about the total count of a distinct third item (uncomment if needed)
                            for k in range(number_of_objects):
                                if k != i and k != j:
                                    object_3 = sampled_items[k]
                                    question_obj3 = f"If a person takes away {count_1} {object_1 if count_1 == 1 else plural_dictionary[object_1]} and {count_2} {object_2 if count_2 == 1 else plural_dictionary[object_2]}, How many total {plural_dictionary[object_3]} remain in the image?"
                                    answer_obj3 = question_items[object_3]
                                    qa_pairs.append({
                                        "question": question_obj3,
                                        "answer": answer_obj3,
                                    })

    return qa_pairs



def multiple_operations_two_ops_extended(number_of_objects, sampled_items, question_items):
    qa_pairs = []
    operations = ["add", "takeaway"]

    # Choose a random number of objects for each scenario (between 1 to max_objects)
    for num_selected_objects in range(1, min(6, number_of_objects + 1)):  # Ensure we don't exceed the number of available objects
        selected_objects = random.sample(sampled_items, num_selected_objects)

        # Ensure we have at least two objects to perform two operations
        if len(selected_objects) >= 2:
            for count_1 in range(1, 4):  # Operation on first object
                for count_2 in range(1, 4):  # Operation on second object

                    # Randomize the operations and objects
                    op_1, op_2 = random.sample(operations, 2)
                    object_1, object_2 = random.sample(selected_objects, 2)

                    # Check for valid operations
                    if (op_1 == "takeaway" and question_items[object_1] - count_1 < 0) or \
                       (op_2 == "takeaway" and question_items[object_2] - count_2 < 0):
                        continue

                    # Construct the question based on the operations
                    question = f"If a person {op_1}s {count_1} {object_1 if count_1 == 1 else plural_dictionary[object_1]} and {op_2}s {count_2} {object_2 if count_2 == 1 else plural_dictionary[object_2]}, "

                    # Determine the answers based on the operations
                    answer_1 = question_items[object_1] + count_1 if op_1 == "add" else question_items[object_1] - count_1
                    answer_2 = question_items[object_2] + count_2 if op_2 == "add" else question_items[object_2] - count_2

                    # Randomly choose which object's count to ask about
                    queried_object = random.choice(selected_objects)
                    question += f"How many total {plural_dictionary[queried_object]} are there in the image?"
                    answer = question_items[queried_object]
                    if queried_object == object_1:
                        answer = answer_1
                    elif queried_object == object_2:
                        answer = answer_2

                    qa_pairs.append({
                        "question": question,
                        "answer": answer,
                    })

    return qa_pairs


def quantitative_comparison(number_of_objects, sampled_items, question_items):
    qa_pairs = []

    for i in range(number_of_objects):
        object_1 = sampled_items[i]  # The item being taken away or added
        for j in range(number_of_objects):
            if i != j:  # Ensure object_1 and object_2 are different
                object_2 = sampled_items[j]  # The item being compared to

                for count in range(1, 4):  # Taking away 1, 2, or 3 of object_1
                    # For subtraction, ensure that it won't lead to negative counts
                    if question_items[object_1] - count >= 0:
                        question_sub = f"After taking away {count} {object_1 if count == 1 else plural_dictionary[object_1]}, are there more {plural_dictionary[object_1]} than {plural_dictionary[object_2]}?"
                        answer_sub = "Yes" if question_items[object_1] - count > question_items[object_2] else "No"
                        qa_pairs.append({
                            "question": question_sub,
                            "answer": answer_sub,
                        })

                    # For addition
                    question_add = f"After adding {count} {object_1 if count == 1 else plural_dictionary[object_1]}, are there more {plural_dictionary[object_1]} than {plural_dictionary[object_2]}?"
                    answer_add = "Yes" if question_items[object_1] + count > question_items[object_2] else "No"
                    qa_pairs.append({
                        "question": question_add,
                        "answer": answer_add,
                    })

    return qa_pairs


def quantitative_comparison_multiple_ops(number_of_objects, sampled_items, question_items):
    qa_pairs = []

    for i in range(number_of_objects):
        for j in range(number_of_objects):
            if i != j:  # Ensure object_1 and object_2 are different
                object_1 = sampled_items[i]  # The first item for the operation
                object_2 = sampled_items[j]  # The second item for the operation

                for count_1 in range(1, 4):  # Operation on first object
                    for count_2 in range(1, 4):  # Operation on second object

                        # For subtraction, ensure that it won't lead to negative counts
                        if question_items[object_1] - count_1 >= 0 and question_items[object_2] - count_2 >= 0:
                            question_sub = f"After taking away {count_1} {object_1 if count_1 == 1 else plural_dictionary[object_1]} and {count_2} {object_2 if count_2 == 1 else plural_dictionary[object_2]}, are there more {plural_dictionary[object_1]} than {plural_dictionary[object_2]}?"
                            answer_sub = "Yes" if question_items[object_1] - count_1 > question_items[object_2] - count_2 else "No"
                            qa_pairs.append({
                                "question": question_sub,
                                "answer": answer_sub,
                            })

                        # For addition
                        question_add = f"After adding {count_1} {object_1 if count_1 == 1 else plural_dictionary[object_1]} and {count_2} {object_2 if count_2 == 1 else plural_dictionary[object_2]}, are there more {plural_dictionary[object_1]} than {plural_dictionary[object_2]}?"
                        answer_add = "Yes" if question_items[object_1] + count_1 > question_items[object_2] + count_2 else "No"
                        qa_pairs.append({
                            "question": question_add,
                            "answer": answer_add,
                        })

    return qa_pairs



def existential_questions(number_of_objects, sampled_items, question_items):
    qa_pairs = []

    for i in range(number_of_objects):
        object_1 = sampled_items[i]  # The item being taken away or added

        for count in range(1, 4):  # Taking away 1, 2, or 3 of object_1
            # For subtraction, ensure that it won't lead to negative counts
            if question_items[object_1] - count >= 0:
                question_sub = f"If {count} {object_1 if count == 1 else plural_dictionary[object_1]} are taken away, are there at least 2 {plural_dictionary[object_1]} left?"
                answer_sub = "Yes" if question_items[object_1] - count >= 2 else "No"
                qa_pairs.append({
                    "question": question_sub,
                    "answer": answer_sub,
                })

            # For addition
            question_add = f"If {count} {object_1 if count == 1 else plural_dictionary[object_1]} are added, are there at least 2 {plural_dictionary[object_1]}?"
            answer_add = "Yes" if question_items[object_1] + count >= 2 else "No"
            qa_pairs.append({
                "question": question_add,
                "answer": answer_add,
            })

    return qa_pairs


def existential_questions_multiple_ops(number_of_objects, sampled_items, question_items):
    qa_pairs = []

    for i in range(number_of_objects):
        object_1 = sampled_items[i]  # The first item for the operation
        for j in range(number_of_objects):
            if i != j:  # Ensure object_1 and object_2 are different
                object_2 = sampled_items[j]  # The second item for the operation

                for count_1 in range(1, 4):  # Operation on first object
                    for count_2 in range(1, 4):  # Operation on second object

                        # For subtraction, ensure that it won't lead to negative counts
                        if question_items[object_1] - count_1 >= 0 and question_items[object_2] - count_2 >= 0:
                            question_sub = f"If {count_1} {object_1 if count_1 == 1 else plural_dictionary[object_1]} are taken away and {count_2} {object_2 if count_2 == 1 else plural_dictionary[object_2]} are added, are there at least 2 {plural_dictionary[object_1]}?"
                            answer_sub = "Yes" if question_items[object_1] - count_1 + count_2 >= 2 else "No"
                            qa_pairs.append({
                                "question": question_sub,
                                "answer": answer_sub,
                            })

                        # For addition
                        question_add = f"If {count_1} {object_1 if count_1 == 1 else plural_dictionary[object_1]} are added and {count_2} {object_2 if count_2 == 1 else plural_dictionary[object_2]} are taken away, are there at least 2 {plural_dictionary[object_1]}?"
                        answer_add = "Yes" if question_items[object_1] + count_1 - count_2 >= 2 else "No"
                        qa_pairs.append({
                            "question": question_add,
                            "answer": answer_add,
                        })

    return qa_pairs



def percentage_proportional_questions(number_of_objects, sampled_items, question_items):
    qa_pairs = []

    for i in range(number_of_objects):
        object_1 = sampled_items[i]  # The item being affected

        # Subtraction by half
        if question_items[object_1] > 1:  # At least two items needed for 'half'
            count_sub = math.ceil(question_items[object_1] / 2)  # Round up to the nearest integer
            question_sub = f"If half of the {plural_dictionary[object_1]} are taken away, how many remain?"
            answer_sub = question_items[object_1] - count_sub
            qa_pairs.append({
                "question": question_sub,
                "answer": answer_sub,
            })

        # Addition by doubling
        question_add = f"If the number of {plural_dictionary[object_1]} is doubled, how many will there be?"
        answer_add = question_items[object_1] * 2
        qa_pairs.append({
            "question": question_add,
            "answer": answer_add,
        })

    return qa_pairs

def percentage_proportional_questions_multiple_ops(number_of_objects, sampled_items, question_items):
    qa_pairs = []

    for i in range(number_of_objects):
        object_1 = sampled_items[i]  # The first item for the percentage-based operation
        for j in range(number_of_objects):
            if i != j:  # Ensure object_1 and object_2 are different
                object_2 = sampled_items[j]  # The second item for the operation

                # Subtraction by half for object_1
                if question_items[object_1] > 1:  # At least two items needed for 'half'
                    count_sub_1 = math.ceil(question_items[object_1] / 2)  # Round up to the nearest integer
                    for count_2 in range(1, 4):  # Operation on second object

                        # For subtraction, ensure it won't lead to negative counts for object_2
                        if question_items[object_2] - count_2 >= 0:
                            question_sub = f"If half of the {plural_dictionary[object_1]} are taken away and {count_2} {object_2 if count_2 == 1 else plural_dictionary[object_2]} are taken away, how many {plural_dictionary[object_1]} are there?"
                            answer_sub = question_items[object_1] - count_sub_1
                            qa_pairs.append({
                                "question": question_sub,
                                "answer": answer_sub,
                            })

                        # For addition on object_2
                        question_add = f"If half of the {plural_dictionary[object_1]} are taken away and {count_2} {object_2 if count_2 == 1 else plural_dictionary[object_2]} are added, how many {plural_dictionary[object_1]} are there?"
                        answer_add = question_items[object_1] - count_sub_1
                        qa_pairs.append({
                            "question": question_add,
                            "answer": answer_add,
                        })

                # Addition by doubling for object_1
                for count_2 in range(1, 4):  # Operation on second object
                    # For subtraction, ensure it won't lead to negative counts for object_2
                    if question_items[object_2] - count_2 >= 0:
                        question_sub = f"If the number of {plural_dictionary[object_1]} is doubled and {count_2} {object_2 if count_2 == 1 else plural_dictionary[object_2]} are taken away, how many {plural_dictionary[object_1]} are there?"
                        answer_sub = question_items[object_1] * 2
                        qa_pairs.append({
                            "question": question_sub,
                            "answer": answer_sub,
                        })

                    # For addition on object_2
                    question_add = f"If the number of {plural_dictionary[object_1]} is doubled and {count_2} {object_2 if count_2 == 1 else plural_dictionary[object_2]} are added, how many {plural_dictionary[object_1]} are there?"
                    answer_add = question_items[object_1] * 2
                    qa_pairs.append({
                        "question": question_add,
                        "answer": answer_add,
                    })

    return qa_pairs

# def cause_effect_questions(number_of_objects, sampled_items, question_items):
#     qa_pairs = []

#     for i in range(number_of_objects):
#         object_1 = sampled_items[i]  # The item being added or taken away
#         for j in range(number_of_objects):
#             if i != j:  # Ensure object_1 and object_2 are different
#                 object_2 = sampled_items[j]  # The item being compared to

#                 for count in range(1, 4):  # Adding or taking away 1, 2, or 3 of object_1
#                     # For subtraction, ensure that it won't lead to negative counts
#                     if question_items[object_1] - count >= 0:
#                         question_sub = f"If a person were to take away {count} {object_1 if count == 1 else plural_dictionary[object_1]}, would there be more {plural_dictionary[object_1]} than {plural_dictionary[object_2]}?"
#                         answer_sub = "Yes" if question_items[object_1] - count > question_items[object_2] else "No"
#                         qa_pairs.append({
#                             "question": question_sub,
#                             "answer": answer_sub,    
#                             })

#     return qa_pairs


def math_mixed_questions(number_of_objects, sampled_items, question_items):
    qa_pairs = []
    # Mixed Scenarios: Grouping and Distributing Items
    for i in range(number_of_objects):
        object_1 = sampled_items[i]  # The item being grouped or distributed

        # Grouping
        for group_size in range(2, 5):  # Grouping in sizes of 2, 3, or 4
            total_groups = question_items[object_1] // group_size
            remainder = question_items[object_1] % group_size
            question = f"If you were to arrange the {plural_dictionary[object_1]} in groups of {group_size}, how many groups will you have?"
            answer = total_groups
            qa_pairs.append({
                "question": question,
                "answer": answer,
            })

            # Check if there are any items left out of the grouping
            if remainder > 0:
                question_remainder = f"If you were to arrange all the {plural_dictionary[object_1]} in groups of {group_size}, how many {plural_dictionary[object_1]} would be left out?"
                answer_remainder = remainder
                qa_pairs.append({
                    "question": question_remainder,
                    "answer": answer_remainder,
                })

        # Distributing among other items
        for j in range(number_of_objects):
            if i != j:
                object_2 = sampled_items[j]  # The item among which object_1 is distributed
                if question_items[object_2] > 0:  # Ensure there is at least one object_2 to distribute among
                    items_per_object_2 = question_items[object_1] // question_items[object_2]
                    question_distribute = f"If you distribute the {plural_dictionary[object_1]} equally among the {plural_dictionary[object_2]}, how many {plural_dictionary[object_1]} will each {object_2} have?"
                    answer_distribute = items_per_object_2
                    qa_pairs.append({
                        "question": question_distribute,
                        "answer": answer_distribute,
                    })

    return qa_pairs




def create_sum_QA(question_items, object_key):
    qa_pairs = []
    question_templates = [
        "How many total {object_plural} are there in the image?",
        # "What is the total number of {object_plural} in the given image?"
    ]

    answer = sum(list(question_items.values()))
    sampled_question_template = random.choice(question_templates)
    question = sampled_question_template.format(object_plural=plural_dictionary[object_key])
    qa_pairs.append({
        "question": question,
        "answer": answer,
    })
    return qa_pairs


def two_items_equal_comparison(number_of_objects, sampled_items, question_items):
    qa_pairs = []
    question_templates = [
        "Are there equal number of {object_1} and {object_2} in the image?",
    ]

    for i in range(number_of_objects):
        for j in range(i + 1, number_of_objects):
            sampled_question_template = random.choice(question_templates)
            object_1, object_2 = plural_dictionary[sampled_items[i]], plural_dictionary[sampled_items[j]]

            question = sampled_question_template.format(object_1=object_1, object_2=object_2)
            answer = "No"
            if (question_items[sampled_items[i]] == question_items[sampled_items[j]]):
                answer = "Yes"
            qa_pairs.append({
                "question": question,
                "answer": answer
            })
    return qa_pairs


def create_QA():

    obj_to_return = []
    total_questions = 0
    
    object_keys = list(object_dictionary.keys())
    
    # object_keys = ["fruit", "vegetable", "animal"]
    

    for object_key in object_keys:
        #object_key = "fruit"
        
        object = object_dictionary[object_key]
        #object = ["items", "range"]

        items = object["items"]
        
        #items = ["apple", "orange", "banana", "strawberry", "grape"]
        
        items_range = object["range"]
        #items_range = [1, 5]

        for L in range(1, len(items) + 1):
            # L = [1, 2, 3, 4, 5]
            # L = 1  
            
            for sampled_items in itertools.combinations(items, L):
                
                number_of_objects = len(sampled_items)
                
                #number_of_objects = 2
                
                #sampled_items = ["apple", "orange"]
                
                item_count_values = [i for i in range(items_range[0], items_range[1] + 1)]
                
                # item_count_values = [1, 2, 3, 4, 5]
                
                lists = [item_count_values]*number_of_objects
                
                #lists = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
                
                for combination in itertools.product(*lists):
                    #combination = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]
                                        
                    index = 0
                    qa_pairs = []
                    question_item = {}
                    for item in sampled_items:
                        item_count = combination[index]
                        question_item[item] = item_count
                        index += 1

                    
                    #question item --> {"apple": 1, "orange": 2}
                    #qa_pairs = {"question": "How many total apples are there in the image?", "answer": 1}
                    
                    
                    # qa_pairs += create_sum_QA(question_item, object_key)
                    # qa_pairs += two_items_equal_comparison(number_of_objects, sampled_items, question_item)
    #97k Question   # qa_pairs += positive_add_items_to_object(number_of_objects, sampled_items, question_item)
    #324k           # qa_pairs +=negative_add_items_to_object_v2(number_of_objects, sampled_items, question_item)
    #5929k            qa_pairs += complex_add_items_to_object(number_of_objects, sampled_items, question_item)
                    
                    # qa_pairs += multiple_operations_two_ops_extended(number_of_objects, sampled_items, question_item)
                    # qa_pairs += quantitative_comparison(number_of_objects, sampled_items, question_item)
                    # qa_pairs += existential_questions(number_of_objects, sampled_items, question_item)
                    # qa_pairs += percentage_proportional_questions(number_of_objects, sampled_items, question_item)
                    # qa_pairs += cause_effect_questions(number_of_objects, sampled_items, question_item)
                    
                    
                    obj_to_return.append({
                        "obj_json": question_item,
                        "qa_pairs": qa_pairs,
                    })
                    total_questions += len(qa_pairs)
    print(len(obj_to_return), total_questions)
    return obj_to_return


if __name__ == "__main__":
    create_QA()
