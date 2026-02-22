# 最初に戻るためのwhile
while True:
# 辞書作成
    drinks = {"コーラ": 120, "水": 80, "お茶":100}
    print(drinks)
# while True: (正しいメニューが入力されるまで、入力を繰り返す)
    while True:
# input()でユーザーに購入する飲み物を入力させる
        drink = input("購入する飲み物を選んでください")
# drink in drinks: で入力された飲み物が辞書にあるか確認
        if drink in drinks:
            break
# 入力が間違っている場合 else:(辞書に無い商品の場合もう一度入力)
        else:
            print("違います")
# ユーザーが選んだ飲み物を辞書から取り出してprice(変数)に代入
    price = drinks[drink]

    while True:
    # ユーザーに投入金額を入力させる
        money_input = input("金額を入力してください")
    # 金額が入力されているか確認 ※""は空の文字列
        if money_input == "":
            print("金額を入力してください")
    # continueでこのループの先頭に戻る
            continue
    # 文字を数値に変える(計算できるように数値に変換)
        money = int(money_input)
    # 投入金額が価格より足りない場合再入力させる
        if money < price:
            print("金額がたりません")
            # 金額が足りないからもう1度購入をする
            continue
        # 金額の入力ループ終了し次へ
        break 

    while True:
        # 投入金額が価格より少ないかチェック
        if money < price:
        # 不足(lack)している金額の計算
            lack = price - money
            print("あと" + str(lack) + "円足りません")
        else:
        # 投入金額から商品の値段を引いたお釣り(change)の計算
            change = money - price
            print("購入できました")
            print("お釣りは" + str(change) + "円です")
            break
    # 再び購入するかユーザーに確認
    again = input("続けますか?(yes/no):")
    # noと入力されたら終了する
    if again == "no":
        print("終了します")
        break
    # yseと入力されたら最初に戻って購入処理
    elif again == "yes":
        print("もう一度購入します")
        continue
    # yse/no以外が入力された時のエラーメッセージ
    else:
        print("yesかnoを入力してください")
