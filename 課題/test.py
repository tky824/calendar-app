# 辞書作成
drinks = {"コーラ": 120, "水": 80, "お茶":100}
print(drinks)
# while文で繰り返し処理
# while True: (正しいメニューが入力されるまで、入力を繰り返す)
while True:
# input()でユーザーに入力させる
    drink = input("購入する飲み物を選んでください")
# drink in drinks: でメニューに存在
    if drink in drinks:
        break
# breakでループから抜けて次の処理(止める)
    else:
        print("違います")
# 入力が間違っている場合 else:

# whileで再入力
while True:
# input()でユーザーに金額を入力させる
    money_input = input("金額を投入してください:")
# 数字かどうか？　okならTrue
is_number = True
if money_input == "":
# 間違っていればFalse
    is_number = False
while True:
# 金額を入力させる↓
     money_input = input("金額を投入してください:")
     money = int(money_input)
# 数字に変換できるようにする
     break
while True:
# 金額を入力させる(金額が足りるまで、入力を繰り返す)
     money_input = input("金額を入力してください")
     print(money_input)
# 金額が入力されているか確認 ※""は空の文字列
     if money_input == "":
         print("金額を入力してください")
     else:
          print("入力されました")
          break
# 文字を数値に変える
money = int(money_input)
# 投入金額が価格より少ないかチェック
if money < price:
     print("金額がたりません")
else:
     print("購入できます")     

while True:
# 投入金額が価格より少ないかチェック
     if money < price:
# 不足(lack)している金額の計算
         lack = price - money
         print("あと" + str(lack) + "円足りません")
     else:
     # お釣り(change)の計算
          change = money - price
          print("購入できました")
          print("お釣りは" + str(change) + "円です")
          break
while True:
    # 再び購入するかユーザーにチェック
     again = input("続けますか?(yes/no):")
     # noと入力されたら終了する
     if again == "no":
          print("終了します")
          break