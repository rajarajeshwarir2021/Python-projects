import os

folder_name = "../files"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

ht_list = []

while True:
    user_input = input("Throw the coin and enter head or tail here: ? ").lower() + '\n'
    ht_list.append(user_input)
    h_prob = (ht_list.count("head\n") / (ht_list.count("head\n") + ht_list.count("tail\n"))) * 100
    print(f"Heads: {h_prob}%")

    file_path = os.path.join(folder_name, "ProbabilityGame.txt")

    with open(file_path, 'w') as fh:
        fh.writelines(ht_list)