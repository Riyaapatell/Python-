# quiz game
questions = [
    {
        "question":"hi",
        "options":["A. Hello", "B. Hello", "C. Hello", "D. Hello"],
        "ans":"B"
        },
    {
            "question":"hi",
            "options":["A. Hello", "B. Hello", "C. Hello", "D. Hello"],
            "ans":"B"
    }

]
score = 0
print("-----Quiz-----")
for i, quiz in enumerate(questions,1):
    # print("Q", i, ".", quiz["question"])
    print(f"Q{i}. {quiz["question"]}")
    for option in quiz["options"]:
        print(option)
    answer = input("Enter your answer: ").upper()

    if answer == quiz["ans"]:
        print("Correct")
        score += 1
    else:
        print("Answer is incorrect. Correct answer is",quiz["ans"])
    print("----")

print("Your score:",score,"/10 ")