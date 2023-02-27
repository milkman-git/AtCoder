# Atcordbr Beginners Selection
# ABC087B - Coins
# 枚数のインプットと合計金額の入力
Coin_500: int = int(input())
Coin_100: int = int(input())
Coin_50: int = int(input())
Coin_Sum: int = int(input())
# コイン枚数の総数
Count_Comb: int = 0

# 各種枚数が最小の値から入力の値まで総当たり
for Count_500 in range(Coin_500 + 1):
    for Count_100 in range(Coin_100 + 1):
        for Count_50 in range(Coin_50 + 1):
            if Coin_Sum == 500 * Count_500 + 100 * Count_100 + 50 * Count_50:
                Count_Comb += 1

print(Count_Comb)
