questions = {
    "Python was created by?": "guido",
    "What keyword defines a function?": "def",
    "What type stores key-value pairs?": "dict"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question + " ").lower()

    if user_answer == answer:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")

print(f"\nScore: {score}/{len(questions)}")
print("Percentage:", round(score / len(questions) * 100, 2), "%")
