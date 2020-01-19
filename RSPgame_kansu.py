import random
enemy = random.randint(1, 3)
#とりあえず関数版
def rsp(player):
    if player == 1:
        print("あなたはグーを出しました")
        if enemy == 1:
            print("あいてはグーを出しました")
            print("あいこです")
        elif enemy == 2:
            print("あいてはチョキを出しました")
            print("あなたの勝ちです")
        elif enemy == 3:
            print("あいてはパーを出しました")
            print("あなたの負けです") 
    elif player == 2:
        print("あなたはチョキを出しました")
        if enemy == 1:
            print("あいてはグーを出しました")
            print("あなたの負けです")
        elif enemy == 2:
            print("あいてはチョキを出しました")
            print("あいこです")
        elif enemy == 3:
            print("あいてはパーを出しました")
            print("あなたの勝ちです") 
    elif player == 3:
        print("あなたはパーを出しました")
        if enemy == 1:
            print("あいてはグーを出しました")
            print("あなたの勝ちです")
        elif enemy == 2:
            print("あいてはチョキを出しました")
            print("あなたの負けです")
        elif enemy == 3:
            print("あいてはパーを出しました")
            print("あいこです") 
    else:
        print("エラーです。")

def main():
    retry = "y"
    while 1:
        if retry == "y":
            print("グーなら1、チョキなら２、パーなら３を入力してください\n勝ち負け引き分けの結果が出力されます\n123以外の入力がされた場合にはエラーが出力されます")
            player_input = input("1~3を入力してください")#ここで数以外を入力するとエラーが出て止まってしまう
            player = int(player_input)
            print(rsp(player))#実行するとこの後にnoneが出てきた後にもう一回しますか？が出てくる。noneが出ないようにしたい
            print("もう一回しますか？")
            retry = input("y/n")
        elif retry == "n":
            break
        else:
            print("エラーです。yかnを入力して下さい")
            retry = input("y/n")

    

if __name__ == '__main__':
    main()
