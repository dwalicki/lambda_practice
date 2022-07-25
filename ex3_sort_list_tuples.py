# Write a Python program to sort a list of tuples using Lambda

dota_heroes = [
    ("Axe", 6),
    ("Shadow Fiend", 5),
    ("Marci", 2),
    ("Crystal Maiden", 3),
    ("Viper", 1),
    ("Meepo", 4),
]
print(dota_heroes)

sortedList = sorted(dota_heroes, key=lambda x: x[1], reverse=True)
print("Sorted List: ", sortedList)


SelectHeroes = sorted(dota_heroes, key=lambda x: x[1])

print(SelectHeroes)
