# Atcordbr Beginners Selection
# ABC083B - Some Sums
# 整数と各桁の和(最小Ａ最大Ｂ)の入力
n, a, b = map(int, input().split())
# 合計値格納
sum = 0

# n以下の整数に対して
for num in range(n + 1):
    keta_sum = 0
    tmp = num
    # 各桁の合計値を計算
    while True:
        tmp = tmp // 10
        if (tmp < 1):
            break
        keta_sum += tmp % 10   
    
    # 桁合計値がa以上b以下ならば合計計算
    if (a <= (keta_sum + (num % 10)) <= b):
        sum += num

print(sum)
