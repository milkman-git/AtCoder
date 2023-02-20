# Atcordbr Beginners Selection
# PracticeA - ABC086A - Product
stdin_a: int
stdin_b: int
stdin_a, stdin_b = map(int, input().split())
if (1 <= stdin_a <= 10000 or 1 or 1 <= stdin_b <= 10000):
    if ((stdin_a * stdin_b) % 2 == 1):
        print("Odd")
    else:
        print("Even")
