# Atcordbr Beginners Selection
# ABC081B - Shift only
input()
origin_board = list(map(int, input().split()))
origin_count = len(origin_board)
div_count = 0
while True:
    # ボードの中身を精査し、割り切れない数があればbreak
    origin_board = filter(lambda x: x % 2 == 0, origin_board)
    origin_board = list(origin_board)
    if (origin_count != len(origin_board)):
        break

    # ボードの中身を割り込みして、割った回数を増加    
    origin_board = list(map(lambda x: x / 2, origin_board))
    div_count += 1

print(div_count)
