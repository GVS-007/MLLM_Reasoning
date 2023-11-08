import random
random.seed(42)

def incomplete_questions(question_items, object_type):
    sample_item = random.choice(list(question_items.keys()))
    question = f"If an object is taken away at random, what is the count of {sample_item}s now in the image?"
    answer = "Cannot answer based on this information."
    
    return [{
        "question": question,
        "answer": answer,
        "question_type": "incomplete_information",
        "answer_type" : "string",
        "category_type": object_type,
        "source_function": "incomplete_question"
    }]
