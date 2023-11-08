def spatial_reasoning_questions(question_items, object_type):
    qa_pairs = []
    
    # Sorting items based on count and name for a simulated spatial arrangement
    ordered_items = sorted(question_items.keys(), key=lambda x: (question_items[x], x))
    
    for idx, item in enumerate(ordered_items):
        # For questions about the relative position of items
        if idx < len(ordered_items) - 1:
            question_1 = f"Based on the frequency arrangement from left to right, is the {item} placed to the left of the {ordered_items[idx+1]} in the image?"
            answer_1 = "Yes"  # Because of the sorting, the answer will always be yes.
            qa_pairs.append({
                "question": question_1,
                "answer": answer_1,
                "question_type": "spatial_reasoning",
                "answer_type": "boolean",
                "category_type": object_type,
                "source_function": "generate_spatial_reasoning_questions"
            })
        
        # For the center item question
        if len(ordered_items) % 2 == 1 and idx == len(ordered_items) // 2:
            question_2 = f"In the left-to-right frequency arrangement, which item is at the center in the image?"
            answer_2 = item
            qa_pairs.append({
                "question": question_2,
                "answer": answer_2,
                "question_type": "spatial_reasoning",
                "answer_type": "string",
                "category_type": object_type,
                "source_function": "generate_spatial_reasoning_questions"
            })
        
        # For the question about the item to the left of the current item
        if idx > 0:
            question_3 = f"Which object is immediately to the left of the {item} in the image?"
            answer_3 = ordered_items[idx-1]
            qa_pairs.append({
                "question": question_3,
                "answer": answer_3,
                "question_type": "spatial_reasoning",
                "answer_type": "string",
                "category_type": object_type,
                "source_function": "generate_spatial_reasoning_questions"
            })
        
        second_to_right = None
        third_to_left = None

        if idx < len(ordered_items) - 2:
            second_to_right = ordered_items[idx + 2]
            question_p = f"Which object is second to the right of the {item} in the image, circle back to the beginning if we exceed the available objects in the arrangement?"
            answer_p = second_to_right
            qa_pairs.append({
                "question": question_p,
                "answer": answer_p,
                "question_type": "spatial_reasoning",
                "answer_type": "string",
                "category_type": object_type,
                "source_function": "generate_spatial_reasoning_questions"
            })

        # Check if there is an item third to the left
        if idx >= 2:
            third_to_left = ordered_items[idx - 3]
            question_t = f"Which object is third to the left of the {item} in the image, circle back to the end if we exceed the available objects in the arrangement?"
            answer_t = third_to_left
            qa_pairs.append({
                "question": question_t,
                "answer": answer_t,
                "question_type": "spatial_reasoning",
                "answer_type": "string",
                "category_type": object_type,
                "source_function": "generate_spatial_reasoning_questions"
            })
            

        # For questions about the relative position of items
        if idx < len(ordered_items) - 1:
            question_1 = f"Based on the frequency arrangement from top to bottom, is the {item} placed above the {ordered_items[idx+1]} in the image?"
            answer_1 = "Yes"  # Because of the sorting, the answer will always be yes.
            qa_pairs.append({
                "question": question_1,
                "answer": answer_1,
                "question_type": "spatial_reasoning",
                "answer_type": "boolean",
                "category_type": object_type,
                "source_function": "generate_spatial_reasoning_questions"
            })
        
        # For the center item question
        if len(ordered_items) % 2 == 1 and idx == len(ordered_items) // 2:
            question_2 = f"In the top-to-bottom frequency arrangement, which object is at the center in the image?"
            answer_2 = item
            qa_pairs.append({
                "question": question_2,
                "answer": answer_2,
                "question_type": "spatial_reasoning",
                "answer_type": "string",
                "category_type": object_type,
                "source_function": "generate_spatial_reasoning_questions"
            })
        
        # For the question about the item above the current item
        if idx > 0:
            question_3 = f"Which object is immediately above the {item} in the image?"
            answer_3 = ordered_items[idx-1]
            qa_pairs.append({
                "question": question_3,
                "answer": answer_3,
                "question_type": "spatial_reasoning",
                "answer_type": "string",
                "category_type": object_type,
                "source_function": "generate_spatial_reasoning_questions"
            })
    
    return qa_pairs
