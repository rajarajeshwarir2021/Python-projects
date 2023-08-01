rate = 0.95
dollars = float(input("How many dollars have you got?"))
euros = rate * dollars
print(f"The amount in euros is:\n{euros}")

ranking  = ['John', 'Sen', 'Lisa']
rank = int(input("Enter rank number: ")) - 1
name = ranking[rank]
print(name)

name = input("Enter a name: ")
rank = ranking.index(name) + 1
print(rank)