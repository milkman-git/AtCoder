# Atcorder Beginners Selection
# PracticeA - Welcome to AtCoder
try:
    a = int(input())
    b, c = map(int, input().split())
    # splitでは配列が出来上がる。
    # map でb,cに値を返却。
    s = input()
    print("{} {}".format(a + b + c, s))
    # ↑がpythonの書式フォーマットである。
except ValueError:
    print("input is Error.")
