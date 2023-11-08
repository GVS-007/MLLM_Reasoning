
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
    "clock 1" : "clocks",

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

def get_category(sampled_items):
    categories = set()
    for item in sampled_items:
        for category, details in object_dictionary.items():
            if item in details["items"]:
                categories.add(category)
                break
    return categories


def convert_clock_input_to_time(clock_input):
    # Split the input to get the number
    number = clock_input.split()[-1]

    # Convert the number to "o'clock" format
    clock_time = f"{number} o'clock"

    return clock_time

def calculate_hourly_crossings(clock_time):
    # Split the clock time to get the hour
    hour = int(clock_time)

    # Calculate the number of times the minute hand crosses the hour hand to reach 12 o'clock
    crossings = 0
    while hour != 12:
        hour = (hour + 1)
        crossings += 1

    return crossings

def generate_clock_time_questions(question_items, object_type):
    qa_pairs = []

    clock_count = sum(1 for clock_input in question_items if "clock" in get_category([clock_input]))

    if clock_count == 1:
        for clock_input in question_items:
            categories = get_category([clock_input])
            if "clock" in categories:
                clock_time = convert_clock_input_to_time(clock_input)
                # Question: What time does the clock show for "{clock_input}"?
                question = f"If there is a clock in the image, What time does the clock show?"
                answer = clock_time  # The answer is the converted clock time

                # Append the question-answer pair to the list
                qa_pairs.append({
                    "question": question,
                    "answer": answer,
                    "question_type": "clock",
                    "answer_type": "string",
                    "category_type": object_type,
                    "source_function": "generate_clock_time_questions"
                })
            
                question = f"If there is a clock in the image, what time does the clock show after two hours?"
                # Calculate the time after two hours
                current_hour = int(clock_time.split()[0])
                future_hour = (current_hour + 2) % 12
                future_time = f"{future_hour} o'clock"
                answer = future_time

                qa_pairs.append({
                    "question": question,
                    "answer": answer,
                    "question_type": "clock",
                    "answer_type": "string",
                    "category_type": object_type,
                    "source_function": "generate_clock_time_questions"
                })
                
                # Question: If there is a clock, how many times will the minute hand cross the hour hand to reach 12 o'clock?
                question = f"How many times does the hands cross each other when the clock hits 12 o'clock for the first time in the image?"
                # Calculate the number of crossings based on the clock time
                crossings = calculate_hourly_crossings(clock_input.split()[-1])
                answer = crossings

                qa_pairs.append({
                    "question": question,
                    "answer": f"{answer} times",
                    "question_type": "clock",
                    "answer_type": "string",
                    "category_type": object_type,
                    "source_function": "generate_clock_time_questions"
                })

    return qa_pairs
