import random
enemy = random.randint(1, 3)
print("グーなら1、チョキなら２、パーなら３を入力してください\n勝ち負け引き分けの結果が出力されます\n０１２以外の入力がされた場合にはエラーが出力されます")
player_input = input("1~3を入力してください")
player = int(player_input)
if player == 1:
    if enemy == 1:
        print("あいこです")
    elif enemy == 2:
        print("あなたの勝ちです")
    elif enemy == 3:
        print("あなたの負けです") 
elif player == 2:
    if enemy == 1:
        print("あなたの負けです")
    elif enemy == 2:
        print("あいこです")
    elif enemy == 3:
        print("あなたの勝ちです") 
elif player == 3:
    if enemy == 1:
        print("あなたの勝ちです")
    elif enemy == 2:
        print("あなたの負けです")
    elif enemy == 3:
        print("あいこです") 
else:
    print("エラーです。1〜3を入力してください")