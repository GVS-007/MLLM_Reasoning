import random
import numpy as np
import itertools
import math
from math import comb
import random
import numpy as np
import itertools
from datetime import datetime, timedelta

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

import random

def temporal_questions(question_items, object_type):
    qa_pairs = []
    
    # Assuming a range of possible rates for any item.
    possible_rates = list(range(1, 5))  # e.g., John can consume between 1 to 4 of any item per day
    
    person_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"]
    
    for item, count in question_items.items():
        rate = random.choice(possible_rates)
        days = count / rate
        question = f"If {random.choice(person_names)} takes away {rate} {item} each day, how many days will it take to take away all {item}s in the image?"
        
        if days == 1:
            answer = "1 day"
        else:
            answer = f"{int(days)} days" if days == int(days) else f"Approximately {int(days)} days"        
        
        qa_pairs.append({
            "question": question,
            "answer": answer,
            "question_type": "temporal_reasoning",
            "answer_type": "string",
            "category_type": object_type,
            "source_function": "generate_temporal_questions"
        })
    
    for item, count in question_items.items():
        rate = 1
        days = count / rate
        
        # Modified question template 1 (Person Adds)
        double_count = count * 2 - count
        days_to_double = double_count / rate
        
        question_double = f"If {random.choice(person_names)} adds {rate} {item} each day, how many days does it take to double the number of {item}s present in the image?"
        if days_to_double == 1:
            answer = "1 day"
        else:
            answer = f"{int(days_to_double)} days" if days_to_double == int(days_to_double) else f"Approximately {int(days_to_double)} days"        
                
        # Append the doubling quantity question-answer pair
        qa_pairs.append({
            "question": question_double,
            "answer": answer,
            "question_type": "temporal_reasoning",
            "answer_type": "string",
            "category_type": object_type,
            "source_function": "generate_temporal_questions_double"
        })
        
    for item, count in question_items.items():
        rate =  random.choice(possible_rates) # Remove n item per day
        days = count
        
        # Generate a random start date
        start_date = datetime.now() + timedelta(days=random.randint(1, 365))  # Random date within the next year
        
        # Calculate the removal date
        removal_date = start_date + timedelta(days=days)
        
        # Format the removal date in "mmddyyyy" format
        removal_date_str = removal_date.strftime("%m%d%Y")
        
        start_date_str = start_date.strftime("%m/%d/%Y")
        removal_date_str = removal_date.strftime("%m/%d/%Y")
        
        # Modified question template (Removal Start Date)
        question_removal_start = f"If {random.choice(person_names)} starts removing one {item} per day, and they start on {start_date_str}, when does all the {item}s get removed from the image?"
        
        # Append the removal start date question-answer pair
        qa_pairs.append({
            "question": question_removal_start,
            "answer": removal_date_str,
            "question_type": "temporal_reasoning",
            "answer_type": "Date",
            "category_type": object_type,
            "source_function": "generate_temporal_questions_removal_start"
        })
        
    return qa_pairs





