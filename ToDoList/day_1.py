todos = []
user_prompt = "Enter a todo: "

while True:
    text = input(user_prompt)
    todos.append(text)
    print(todos)
    print(type(todos))
