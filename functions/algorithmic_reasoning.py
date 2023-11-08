import random
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

def knapsack(weights, profits, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], profits[i-1] + dp[i-1][w-weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

def knapsack_questions(question_items, object_type):
    weight_values = {}
    profit_values = {}
    
    # Dynamically assign weights and profits for each object type in the image
    for item in question_items.keys():
        weight_values[item] = random.randint(1, 5)
        profit_values[item] = random.randint(1, 10)
    
    weights = [weight_values[item] for item in question_items.keys()]
    profits = [profit_values[item] for item in question_items.keys()]
    counts = [question_items[item] for item in question_items.keys()]
    print(weights, profits, counts)
    expanded_weights = []
    expanded_profits = []
    for w, p, c in zip(weights, profits, counts):
        expanded_weights.extend([w] * c)
        expanded_profits.extend([p] * c)
    
    weight_limit = 15  # Example weight limit, can be adjusted
    max_profit = knapsack(expanded_weights, expanded_profits, weight_limit)
    print(max_profit)
    items_description = ', '.join([f"each {item} weighs {weight_values[item]} units and has a value of {profit_values[item]} units" for item in question_items.keys()])
    question = f"Given that {items_description}, if the weight limit is {weight_limit} units, what's the maximum value John can make in the image?"
    
    return [{
        "question": question,
        "answer": max_profit,
        "question_type": "algorithmic_reasoning",
        "answer_type" : "string",
        "category_type": object_type,
        "source_function": "knapsack_question"
    }]
    
def generate_random_costs(items, seed=42):
    # Set the seed for reproducibility
    random.seed(seed)
    
    # Randomly generate costs between 1 to 5 dollars for the given items
    costs = {}
    for item in items:
        costs[item] = random.randint(1, 5)
    
    return costs

def greedy_algorithm(items, costs, budget):
    items_bought = {}
    total_items = 0
    for item, cost in sorted(costs.items(), key=lambda x: x[1]):
        if item in items and budget >= cost:
            max_items = min(items[item], budget // cost)
            budget -= max_items * cost
            items_bought[item] = max_items
            total_items += max_items
    return total_items, items_bought

# Modify the greedy_question function to generate random costs
def greedy_questions(question_items, object_type):
    costs = generate_random_costs(question_items.keys())
    budget = random.randint(1, 10)
    total_items, items_bought = greedy_algorithm(question_items, costs, budget)
    
    question = f"With a budget of {budget} dollars, following a greedy approach, what's the maximum number of objects you can buy in the image, where " + ", ".join([f"{k} (each costing {costs[k]} dollars)" for k, v in items_bought.items()])
    answer = f"You can buy {total_items} objects"
    
    
    return [{
        "question": question,
        "answer": answer,
        "question_type": "algorithmic_reasoning",
        "answer_type" : "string",
        "category_type": object_type,
        "source_function": "greedy_question"
    }]

def sort_and_median_questions(question_items, object_type):
    sorted_items = sorted(question_items.items(), key=lambda x: x[1], reverse=True)
    mid_idx = len(sorted_items) // 2
    if len(sorted_items) % 2 == 0:  # even
        median_count = (sorted_items[mid_idx-1][1] + sorted_items[mid_idx][1]) / 2
    else:  # odd
        median_count = sorted_items[mid_idx][1]
    # Questions
    question_sort = f"Sort the objects in the image based on their counts in descending order."
    question_median = f"What is the count of the median object in the image?"
    return [
        {
            "question": question_sort,
            "answer": ', '.join([item[0] for item in sorted_items]),
            "answer_type": "string",
            "question_type": "algorithmic_reasoning",
            "answer_type" : "string",
            "category_type": object_type,
            "source_function": "sort_and_median_question"
        },
        {
            "question": question_median,
            "answer": median_count,
            "question_type": "algorithmic_reasoning",
            "answer_type": "float",
            "category_type": object_type,
            "source_function": "sort_and_median_question"
        }
    ]

def count_ways(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)

def recursion_questions(question_items, object_type):
    qa_pairs = []
    
    for item_name, item_count in question_items.items():
        ways = count_ways(item_count)
        question = f"If you can pick 1, 2, or 3 {item_name}s at a time, in how many ways can you pick all the {item_name}s in the image?"
        answer = f"There are {ways} ways."
        
        qa_pairs.append({
            "question": question,
            "answer": answer,
            "question_type": "algorithmic_reasoning",
            "answer_type" : "string",
            "category_type": object_type,
            "source_function": "recursion_question"
        })
    
    return qa_pairs

