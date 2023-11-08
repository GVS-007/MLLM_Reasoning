import random
import itertools
import math
import json

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
        "range": [1, 2]
    },

    # "vegetable": {
    #     "items": [
    #         "carrot",
    #         "broccoli",
    #         "tomato",
    #         "potato",
    #         "cabbage"
    #     ],
    #     "range": [1, 3]
    # },

}
def positive_add_items(number_of_objects, sampled_items, question_items):
    qa_pairs = []
    question_templates = [
        "If a person adds {count} {item_name}, How many total {item_name_1} are there in the image?",
        "If a person adds {count} {item_name}, How many total {super_category_name} are there in the image?"
    ]

    for i in range(number_of_objects):
        object_1 = sampled_items[i]
        
        for count in range(1, 4):
            item_name = object_1 if count == 1 else plural_dictionary[object_1]
            
            for template in question_templates:
                if "super_category_name" in template:
                    super_category = None
                    for category, details in object_dictionary.items():
                        if object_1 in details["items"]:
                            super_category = category
                            break
                    
                    if super_category:
                        super_category_name = plural_dictionary[super_category]
                        question = template.format(count=count, item_name=item_name, super_category_name=super_category_name)
                        answer = sum([question_items.get(item, 0) for item in object_dictionary[super_category]["items"]]) + count
                    else:
                        continue
                else:
                    question = template.format(count=count, item_name=item_name, item_name_1=plural_dictionary[object_1])
                    answer = question_items[object_1] + count
                    
                qa_pairs.append({
                    "question": question,
                    "answer": answer,
                })
    return qa_pairs



def negative_add_items_to_object(number_of_objects, sampled_items, question_items):
    qa_pairs = []
    question_templates = [
        "If a person adds {count} {item_name}, How many total {query_item_name} are there in the image?",
        "If a person adds {count} {item_name}, How many total {super_category_name} are there in the image?"
    ]

    for i in range(number_of_objects):
        object_1 = sampled_items[i]  # The item being added
        
        for j in range(number_of_objects):
            if i != j:
                object_2 = sampled_items[j]

                for count in range(1, 4):
                    item_name = object_1 if count == 1 else plural_dictionary[object_1]
                    query_item_name = plural_dictionary[object_2]

                    for template in question_templates:
                        if "super_category_name" in template:
                            super_category = None
                            for category, details in object_dictionary.items():
                                if object_2 in details["items"]:
                                    super_category = category
                                    break
                            
                            if super_category:
                                super_category_name = plural_dictionary[super_category]
                                question = template.format(count=count, item_name=item_name, super_category_name=super_category_name)
                                if object_1 in object_dictionary[super_category]["items"]:
                                    answer = sum([question_items.get(item, 0) for item in object_dictionary[super_category]["items"]]) + count
                                # answer = sum([question_items.get(item, 0) for item in object_dictionary[super_category]["items"]]) + count
                            else:
                                continue
                        else:
                            question = template.format(count=count, item_name=item_name, query_item_name=query_item_name)
                            answer = question_items[object_2]
                            
                        qa_pairs.append({
                            "question": question,
                            "answer": answer,
                        })
                        
                        
    # print(qa_pairs)
    return qa_pairs

def positive_subtract_items_to_object(number_of_objects, sampled_items, question_items):
    qa_pairs = []
    question_templates = [
        "If a person takes away {count} {item_name}, How many total {item_name_1} remain in the image?",
        "If a person takes away {count} {item_name}, How many total {super_category_name} remain in the image?"
    ]

    for i in range(number_of_objects):
        object_1 = sampled_items[i]
        
        for count in range(1, 4):
            if question_items[object_1] - count >= 0:
                item_name = object_1 if count == 1 else plural_dictionary[object_1]
                
                for template in question_templates:
                    if "super_category_name" in template:
                        super_category = None
                        for category, details in object_dictionary.items():
                            if object_1 in details["items"]:
                                super_category = category
                                break
                        
                        if super_category:
                            super_category_name = plural_dictionary[super_category]
                            question = template.format(count=count, item_name=item_name, super_category_name=super_category_name)
                            if object_1 in object_dictionary[super_category]["items"]:
                                answer = sum([question_items.get(item, 0) for item in object_dictionary[super_category]["items"]]) - count
                            # answer = sum([question_items.get(item, 0) for item in object_dictionary[super_category]["items"]]) - count
                        else:
                            continue
                    else:
                        question = template.format(count=count, item_name=item_name, item_name_1=plural_dictionary[object_1])
                        answer = question_items[object_1] - count
                        
                    qa_pairs.append({
                        "question": question,
                        "answer": answer,
                    })
    return qa_pairs


def negative_subtract_items_to_object(number_of_objects, sampled_items, question_items):
    qa_pairs = []
    question_templates = [
        "If a person takes away {count} {item_name}, How many total {query_item_name} remain in the image?",
        "If a person takes away {count} {item_name}, How many total {super_category_name} remain in the image?"
    ]

    for i in range(number_of_objects):
        object_1 = sampled_items[i]  # The item being taken away
        
        for j in range(number_of_objects):
            if i != j:  # Ensure object_1 and object_2 are different
                object_2 = sampled_items[j]  # The item being asked about

                for count in range(1, 4):  # Taking away 1, 2, or 3 of object_1
                    # Ensure that subtraction won't lead to negative counts for object_1
                    if question_items[object_1] - count >= 0:
                        item_name = object_1 if count == 1 else plural_dictionary[object_1]
                        query_item_name = plural_dictionary[object_2]

                        for template in question_templates:
                            # If the question is about a super category, determine the super category
                            if "super_category_name" in template:
                                super_category = None
                                for category, details in object_dictionary.items():
                                    if object_2 in details["items"]:
                                        super_category = category
                                        break
                                
                                if super_category:
                                    super_category_name = plural_dictionary[super_category]
                                    question = template.format(count=count, item_name=item_name, super_category_name=super_category_name)
                                    answer = sum([question_items.get(item, 0) for item in object_dictionary[super_category]["items"]]) - (count if object_1 in object_dictionary[super_category]["items"] else 0)
                                else:
                                    continue
                            else:
                                question = template.format(count=count, item_name=item_name, query_item_name=plural_dictionary[object_2])
                                answer = question_items[object_2]
                                
                            qa_pairs.append({
                                "question": question,
                                "answer": answer,
                            })

    return qa_pairs



def complex_add_items_to_object(number_of_objects, sampled_items, question_items):
    qa_pairs = []

    question_templates = [
        "If a person adds {count_1} {item_1_name} and {count_2} {item_2_name}, How many total {query_item_name} are there in the image?",
        "If a person adds {count_1} {item_1_name} and {count_2} {item_2_name}, How many total {super_category_name} are there in the image?"
    ]

    for i in range(number_of_objects):
        for j in range(number_of_objects):
            object_1 = sampled_items[i]
            object_2 = sampled_items[j]
            
            for count_1 in range(1, 4):  # Adding 1, 2, or 3 of object_1
                for count_2 in range(1, 4):  # Adding 1, 2, or 3 of object_2
                    item_1_name = object_1 if count_1 == 1 else plural_dictionary[object_1]
                    item_2_name = object_2 if count_2 == 1 else plural_dictionary[object_2]

                    for template in question_templates:
                        for k in range(number_of_objects):
                            # if k == i or k == j:  # The queried item should be different from the two added items
                            #     continue
                            
                            object_3 = sampled_items[k]
                            query_item_name = plural_dictionary[object_3]

                            if "super_category_name" in template:
                                super_category = None
                                for category, details in object_dictionary.items():
                                    if object_3 in details["items"]:
                                        super_category = category
                                        break

                                if super_category:
                                    super_category_name = plural_dictionary[super_category]
                                    question = template.format(count_1=count_1, item_1_name=item_1_name, count_2=count_2, item_2_name=item_2_name, super_category_name=super_category_name)
                                    answer = sum([question_items.get(item, 0) for item in object_dictionary[super_category]["items"]]) + (count_1 if object_1 in object_dictionary[super_category]["items"] else 0) + (count_2 if object_2 in object_dictionary[super_category]["items"] else 0)
                                else:
                                    continue
                            else:
                                question = template.format(count_1=count_1, item_1_name=item_1_name, count_2=count_2, item_2_name=item_2_name, query_item_name=query_item_name)
                                answer = question_items[object_3] + (count_1 if object_1 == object_3 else 0) + (count_2 if object_2 == object_3 else 0)

                            qa_pairs.append({
                                "question": question,
                                "answer": answer,
                            })

    return qa_pairs




def complex_subtract_items_to_object_extended(number_of_objects, sampled_items, question_items):
    qa_pairs = []

    question_templates = [
        "If a person takes away {count_1} {item_1_name} and {count_2} {item_2_name}, How many total {query_item_name} remain in the image?",
        "If a person takes away {count_1} {item_1_name} and {count_2} {item_2_name}, How many total {super_category_name} remain in the image?"
    ]

    for i in range(number_of_objects):
        for j in range(number_of_objects):
            object_1 = sampled_items[i]
            object_2 = sampled_items[j]

            for count_1 in range(1, 4):  # Taking away 1, 2, or 3 of object_1
                for count_2 in range(1, 4):  # Taking away 1, 2, or 3 of object_2

                    # Ensure that subtraction won't lead to negative counts for either object
                    if question_items[object_1] - count_1 >= 0 and question_items[object_2] - count_2 >= 0:
                        item_1_name = object_1 if count_1 == 1 else plural_dictionary[object_1]
                        item_2_name = object_2 if count_2 == 1 else plural_dictionary[object_2]

                        for template in question_templates:
                                for k in range(number_of_objects):
                                    object_3 = sampled_items[k]
                                    super_category = None
                                    
                                    if "super_category_name" in template:
                                        for category, details in object_dictionary.items():
                                            if object_3 in details["items"]:
                                                super_category = category
                                                break

                                        if super_category:
                                            super_category_name = plural_dictionary[super_category]
                                            question = template.format(count_1=count_1, item_1_name=item_1_name, count_2=count_2, item_2_name=item_2_name, super_category_name=super_category_name)
                                            answer = sum([question_items.get(item, 0) for item in object_dictionary[super_category]["items"]]) - (count_1 if object_1 in object_dictionary[super_category]["items"] else 0) - (count_2 if object_2 in object_dictionary[super_category]["items"] else 0)
                                        else:
                                            continue
                                    else:
                                        for k in range(number_of_objects):
                                            object_3 = sampled_items[k]
                                            query_item_name = plural_dictionary[object_3]
                                            question = template.format(count_1=count_1, item_1_name=item_1_name, count_2=count_2, item_2_name=item_2_name, query_item_name=query_item_name)
                                            answer = question_items[object_3] - (count_1 if object_1 == object_3 else 0) - (count_2 if object_2 == object_3 else 0)

                                    qa_pairs.append({
                                        "question": question,
                                        "answer": answer,
                                    })

    return qa_pairs





def multiple_operations_two_ops_extended(number_of_objects, sampled_items, question_items):
    qa_pairs = []
    operations = ["add", "takeaway"]
    question_templates = [
        "If a person {op_1}s {count_1} {item_1_name} and {op_2}s {count_2} {item_2_name}, How many total {query_item_name} are there in the image?",
        "If a person {op_1}s {count_1} {item_1_name} and {op_2}s {count_2} {item_2_name}, How many total {super_category_name} are there in the image?"
    ]

    for num_selected_objects in range(1, min(6, number_of_objects + 1)):
        selected_objects = random.sample(sampled_items, num_selected_objects)

        # Ensure we have at least two objects to perform two operations
        if len(selected_objects) >= 2:
            for object_1 in selected_objects:
                for object_2 in selected_objects:
                    if object_1 != object_2:
                        for count_1 in range(1, 4):  # Operation on first object
                            for count_2 in range(1, 4):  # Operation on second object
                                for op_1 in operations:
                                    for op_2 in operations:
                                        # Check for valid operations
                                        if (op_1 == "takeaway" and question_items[object_1] - count_1 < 0) or \
                                        (op_2 == "takeaway" and question_items[object_2] - count_2 < 0):
                                            continue

                                        for template in question_templates:
                                            for k in range(number_of_objects):
                                                object_3 = sampled_items[k]
                                                super_category = None
                                                
                                                if "super_category_name" in template:
                                                        for category, details in object_dictionary.items():
                                                            if object_3 in details["items"]:
                                                                super_category = category
                                                                break

                                                        if super_category:
                                                            super_category_name = plural_dictionary[super_category]
                                                            question = template.format(op_1=op_1, count_1=count_1, item_1_name=object_1 if count_1 == 1 else plural_dictionary[object_1], op_2=op_2, count_2=count_2, item_2_name=object_2 if count_2 == 1 else plural_dictionary[object_2], super_category_name=super_category_name)
                                                            answer = sum([question_items.get(item, 0) for item in object_dictionary[super_category]["items"]])
                                                            if op_1 == "add" and object_1 in object_dictionary[super_category]["items"]:
                                                                answer += count_1
                                                            elif op_1 == "takeaway" and object_1 in object_dictionary[super_category]["items"]:
                                                                answer -= count_1
                                                            if op_2 == "add" and object_2 in object_dictionary[super_category]["items"]:
                                                                answer += count_2
                                                            elif op_2 == "takeaway" and object_2 in object_dictionary[super_category]["items"]:
                                                                answer -= count_2
                                                        else:
                                                            continue
                                                else:
                                                    queried_object = object_3
                                                    query_item_name = plural_dictionary[queried_object]
                                                    question = template.format(op_1=op_1, count_1=count_1, item_1_name=object_1 if count_1 == 1 else plural_dictionary[object_1], op_2=op_2, count_2=count_2, item_2_name=object_2 if count_2 == 1 else plural_dictionary[object_2], query_item_name=query_item_name)
                                                    answer = question_items[queried_object]
                                                    if op_1 == "add" and queried_object == object_1:
                                                        answer += count_1
                                                    elif op_1 == "takeaway" and queried_object == object_1:
                                                        answer -= count_1
                                                    if op_2 == "add" and queried_object == object_2:
                                                        answer += count_2
                                                    elif op_2 == "takeaway" and queried_object == object_2:
                                                        answer -= count_2

                                                qa_pairs.append({
                                                    "question": question,
                                                    "answer": answer,
                                                })
    
    return qa_pairs
def quantitative_comparison_multiple_ops(number_of_objects, sampled_items, question_items):
    qa_pairs = []
    question_templates = [
        "After {op_1} {count_1} {item_1_name} and {op_2} {count_2} {item_2_name}, are there more {item_name_1} than {item_name_2}?",
        "After {op_1} {count_1} {item_1_name} and {op_2} {count_2} {item_2_name}, are there more {super_category_1} than {super_category_2}?"
    ]
    operations = ["adding", "taking away"]

    for i in range(number_of_objects):
        for j in range(number_of_objects):
            if i != j:  # Ensure distinct items for comparison
                object_1 = sampled_items[i]
                object_2 = sampled_items[j]

                # Identify super categories
                super_category_1 = None
                super_category_2 = None
                for category, details in object_dictionary.items():
                    if object_1 in details["items"]:
                        super_category_1 = category
                    if object_2 in details["items"]:
                        super_category_2 = category

                for count_1 in range(1, 4):
                    for count_2 in range(1, 4):
                        for op_1 in operations:
                            for op_2 in operations:
                                if (op_1 == "taking away" and question_items[object_1] - count_1 < 0) or \
                                   (op_2 == "taking away" and question_items[object_2] - count_2 < 0):
                                    continue

                                # Generate questions and answers
                                item_1_name = object_1 if count_1 == 1 else plural_dictionary[object_1]
                                item_2_name = object_2 if count_2 == 1 else plural_dictionary[object_2]
                                for template in question_templates:
                                    if "super_category_1" in template and super_category_1 == super_category_2:
                                        continue

                                    question = template.format(op_1=op_1, op_2=op_2, count_1=count_1, count_2=count_2, item_1_name=item_1_name, item_2_name=item_2_name, item_name_1=plural_dictionary[object_1], item_name_2=plural_dictionary[object_2], super_category_1=plural_dictionary[super_category_1], super_category_2=plural_dictionary[super_category_2])

                                    if "item_name_1" in template:
                                        if op_1 == "adding":
                                            answer_value_1 = question_items[object_1] + count_1
                                        else:
                                            answer_value_1 = question_items[object_1] - count_1

                                        if op_2 == "adding":
                                            answer_value_2 = question_items[object_2] + count_2
                                        else:
                                            answer_value_2 = question_items[object_2] - count_2

                                        answer = "Yes" if answer_value_1 > answer_value_2 else "No"
                                    else:  # Super category question
                                        super_value_1 = sum(question_items.get(item, 0) for item in object_dictionary[super_category_1]["items"])
                                        super_value_2 = sum(question_items.get(item, 0) for item in object_dictionary[super_category_2]["items"])

                                        if op_1 == "adding":
                                            super_value_1 += count_1
                                        else:
                                            super_value_1 -= count_1

                                        if op_2 == "adding":
                                            super_value_2 += count_2
                                        else:
                                            super_value_2 -= count_2

                                        answer = "Yes" if super_value_1 > super_value_2 else "No"

                                    qa_pairs.append({
                                        "question": question,
                                        "answer": answer,
                                    })

    return qa_pairs



def existential_questions_multiple_ops(number_of_objects, sampled_items, question_items):
    qa_pairs = []
    question_templates = [
        "If {count_1} {item_1_name} are {op_1} and {count_2} {item_2_name} are {op_2}, are there at least 2 {query_item_name}?",
    ]
    operations = ["added", "taken away"]

    for i in range(number_of_objects):
        object_1 = sampled_items[i]
        
        for j in range(number_of_objects):
            if i != j:
                object_2 = sampled_items[j]

                for count_1 in range(1, 4):  # Operation on first object
                    for count_2 in range(1, 4):  # Operation on second object
                        for op_1 in operations:
                            for op_2 in operations:
                                if (op_1 == "taken away" and question_items[object_1] - count_1 < 0) or \
                                   (op_2 == "taken away" and question_items[object_2] - count_2 < 0):
                                    continue

                                item_1_name = object_1 if count_1 == 1 else plural_dictionary[object_1]
                                item_2_name = object_2 if count_2 == 1 else plural_dictionary[object_2]
                                
                                # Generate question for specific item
                                question_item = question_templates[0].format(count_1=count_1, item_1_name=item_1_name, op_1=op_1, count_2=count_2, item_2_name=item_2_name, op_2=op_2, query_item_name=plural_dictionary[object_1])
                                answer_item = "Yes" if (question_items[object_1] + count_1 if op_1 == "added" else question_items[object_1] - count_1) >= 2 else "No"
                                qa_pairs.append({
                                    "question": question_item,
                                    "answer": answer_item,
                                })

                                # Generate question for super category of specific item
                                super_category_1 = None
                                for category, details in object_dictionary.items():
                                    if object_1 in details["items"]:
                                        super_category_1 = category
                                        break

                                super_category_2 = None
                                for category, details in object_dictionary.items():
                                    if object_2 in details["items"]:
                                        super_category_2 = category
                                        break

                                if super_category_1:
                                    total_count = sum([question_items.get(item, 0) for item in object_dictionary[super_category_1]["items"]])
                                    if op_1 == "added":
                                        total_count += count_1
                                    else:
                                        total_count -= count_1
                                        
                                    if op_2 == "added" and super_category_2 == super_category_1:
                                        total_count += count_2
                                    elif op_2 == "taken away" and super_category_2 == super_category_1:
                                        total_count -= count_2
                                    
                                    question_super = question_templates[0].format(count_1=count_1, item_1_name=item_1_name, op_1=op_1, count_2=count_2, item_2_name=item_2_name, op_2=op_2, query_item_name=plural_dictionary[super_category_1])
                                    answer_super = "Yes" if total_count >= 2 else "No"
                                    qa_pairs.append({
                                        "question": question_super,
                                        "answer": answer_super,
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
                    
                    
                    qa_pairs += positive_add_items(number_of_objects, sampled_items, question_item)
                    qa_pairs += negative_add_items_to_object(number_of_objects, sampled_items, question_item)
                    qa_pairs += positive_subtract_items_to_object(number_of_objects, sampled_items, question_item)
                    qa_pairs += negative_subtract_items_to_object(number_of_objects, sampled_items, question_item)
                    qa_pairs += complex_add_items_to_object(number_of_objects, sampled_items, question_item)
                    qa_pairs += complex_subtract_items_to_object_extended(number_of_objects, sampled_items, question_item)
                    qa_pairs += multiple_operations_two_ops_extended(number_of_objects, sampled_items, question_item)
                    qa_pairs += quantitative_comparison_multiple_ops(number_of_objects, sampled_items, question_item)
                    qa_pairs += existential_questions_multiple_ops(number_of_objects, sampled_items, question_item)
                    
                    
                    
                    # qa_pairs += percentage_proportional_questions(number_of_objects, sampled_items, question_item)
                    # qa_pairs += cause_effect_questions(number_of_objects, sampled_items, question_item)
                    
                    
                    obj_to_return.append({
                        "obj_json": question_item,
                        "qa_pairs": qa_pairs,
                    })
                    total_questions += len(qa_pairs)
    # print(len(obj_to_return), total_questions)
    return obj_to_return


if __name__ == "__main__":
    
    
    file_path = 'C:/Users/gunda/Downloads/MLLM_Evaluation_Scale/display.json'
    with open(file_path, 'w') as f:
        json.dump(create_QA(), f)


