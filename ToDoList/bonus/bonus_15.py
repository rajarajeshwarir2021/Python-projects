import json

with open(r"D:\pythonProjects\courseProjects\thePythonMegaCourse\ToDoList\files\questions.json", 'r') as fh:
    dict_data = json.load(fh)

user_score = 0

for question in dict_data:
    print(question['Question_Text'])
    for idx, option in enumerate(question['Options']):
        print(f"{idx + 1} - {option}")

    user_answer = int(input("Enter your answer: "))
    question['User_Answer'] = user_answer

for idx, question in enumerate(dict_data):
    if question['User_Answer'] == question['Answer']:
        user_score = user_score + 1
        result = "Correct Answer"
    else:
        result = "Incorrect Answer"

    print(f"{idx + 1}    User Answer: {question['User_Answer']}, Correct Answer: {question['Answer']}    VERDICT: {result}")

print(f"Score: {user_score}/{len(dict_data)}")