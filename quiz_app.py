# quiz_app.py

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["a) Mumbai", "b) Delhi", "c) Kolkata", "d) Chennai"],
        "answer": "b"
    },
    {
        "question": "Who developed Python?",
        "options": ["a) Dennis Ritchie", "b) James Gosling", "c) Guido van Rossum", "d) Bjarne Stroustrup"],
        "answer": "c"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["a) Central Process Unit", "b) Central Processing Unit", "c) Computer Personal Unit", "d) Central Processor Unit"],
        "answer": "b"
    }
]

score = 0

print("Welcome to the Quiz App!\n")

for i, q in enumerate(questions):
    print(f"Q{i+1}: {q['question']}")
    for option in q["options"]:
        print(option)
    answer = input("Your answer (a/b/c/d): ").lower()
    if answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Correct answer is {q['answer']}.\n")

print(f"Your final score is {score} out of {len(questions)}")