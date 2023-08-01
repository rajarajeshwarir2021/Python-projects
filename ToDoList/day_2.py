user_prompt = "Enter a todo: "
todos = []

while True:
    text = input(user_prompt)
    print(text.title())
    todos.append(text)
