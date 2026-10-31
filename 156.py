# Python Quiz Game using python programming language 

questions = [
    {
        "question": "Which language is used for web development?",
        "options": ["1. Python", "2. HTML", "3. Both"],
        "answer": "3"
    },
    {
        "question": "What is the output of 5 ** 2?",
        "options": ["1. 10", "2. 25", "3. 15"],
        "answer": "2"
    },
    {
        "question": "Which function is used to display output?",
        "options": ["1. input()", "2. print()", "3. type()"],
        "answer": "2"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["1. int", "2. str", "3. bool"],
        "answer": "3"
    }
]

score = 0

print("===== PYTHON QUIZ GAME =====")

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    choice = input("Enter your answer (1/2/3): ")

    if choice == q["answer"]:
        print("Correct answer!")
        score += 1
    else:
        print("Wrong answer!")

print("\n===== QUIZ RESULT =====")
print("Your score:", score, "/", len(questions))
print("Percentage:", (score / len(questions)) * 100, "%")
