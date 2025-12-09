import random

questions = [
    ("What is AI?", ["Artificial Intelligence", "Adobe Illustrator", "Auto Info", "Alien Internet"], "Artificial Intelligence"),
    ("What is CPU?", ["Central Processing Unit", "Control Power Unit", "Core Power Utility", "Central Power Unit"], "Central Processing Unit"),
    ("What is RAM?", ["Random Access Memory", "Run All Memory", "Real Application Memory", "Rapid Access Module"], "Random Access Memory"),
    ("Python is a ___?", ["Programming Language", "Snake", "Toolbox", "Food"], "Programming Language")
]

def get_two_questions():
    return random.sample(questions, 2)

def check_answers(selected, correct):
    return selected == correct
