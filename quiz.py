def quiz():
    questions = {
        "What is the capital of France?": "a",
        "What is 2 + 2?": "b",
        "Which planet is known as the Red Planet?": "c"
    }

    options = {
        "What is the capital of France?": ["a. Berlin", "b. Madrid", "c. Paris", "d. Rome"],
        "What is 2 + 2?": ["a. 3", "b. 4", "c. 5", "d. 6"],
        "Which planet is known as the Red Planet?": ["a. Earth", "b. Jupiter", "c. Mars", "d. Venus"]
    }

    score = 0

    for question in questions:
        print(question)
        for option in options[question]:
            print(option)
        answer = input("Enter your answer (a/b/c/d): ")
        
        if answer == questions[question]:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer.")

    print(f"Your score: {score}/{len(questions)}")

quiz()
