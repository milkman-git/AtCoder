# Atcordbr Beginners Selection
# ABC081A - Placing Marbles
value: str = input()
list = list(value)
count_one: int = 0
for char in list:
    if (char == "1"):
        count_one += 1

print(count_one)
