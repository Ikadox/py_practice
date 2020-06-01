# オブジェクトのコピー（浅いコピーと深いコピー）
# 誤ったオブジェクトコピー
original = [1, [2, 3]]
copy = original
# ↑これは参照値をコピーしただけで、オブジェクトそのものをコピーした訳ではない

# 浅いコピー（スライス機能を使ってコピーしている）
copy = original[:]
copy[0] = 5
print(original[0]) # 1
print(copy[0]) # 5

# 上記の浅いコピーだと、オブジェクトが入れ子になっている場合、完全なコピーができない
copy[1][0] = 7
print(original) # [1, [7, 3]] と出力され、ネストされてる箇所が書き換わっている

# 深いコピー （copy モジュールを使用）
from copy import deepcopy
deep_copy_list = deepcopy(original)
deep_copy_list[1][0] = 9
print(original) # [1, [7, 3]] と出力され、ネストされてる箇所が書き換わってない
print(deep_copy_list) # [1, [9, 3]]