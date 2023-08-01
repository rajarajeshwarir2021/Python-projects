def calculate_age(year_of_birth, current_year = 2023):
    age = current_year - year_of_birth
    return age


birth_year = int(input("What is your year of birth? "))
user_age = calculate_age(birth_year)
#print(user_age)

if user_age > 120:
    print("Congrats! you have crossed a century...")


def num_of_names(name_list):
    name_list = name_list.split(',')
    return len(name_list)


names = input("Enter names separated by commas (no spaces): ")
n_names = num_of_names(names)
print(n_names)