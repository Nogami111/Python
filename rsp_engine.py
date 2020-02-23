# RSP_engine

import random

class Engine:
    def __init__(self, pl='0', ene=random.randint(1, 3), rlt='', ans='y'):
        self.pl = pl
        self.ene = ene
        self.rlt = rlt
        self.ans = ans

    def start(self):
        print("グーなら1、チョキなら２、パーなら３を入力してください\n勝ち負け引き分けの結果が出力されます\n123以外の入力がされた場合にはエラーが出力されます")
        self.pl = input("1~3を入力してください")

    def proc(self):
        if self.pl == '1':
            if self.ene == 1:
                self.rlt = 'あいこ'
            elif self.ene == 2:
                self.rlt = 'あなたの勝ち'
            elif self.ene == 3:
                self.rlt = 'あなたの負け'
        elif self.pl == '2':
            if self.ene == 1:
                self.rlt = 'あなたの負け'
            elif self.ene == 2:
                self.rlt = 'あいこ'
            elif self.ene == 3:
                self.rlt = 'あなたの勝ち'
        elif self.pl == '3':
            if self.ene == 1:
                self.rlt = 'あなたの勝ち'
            elif self.ene == 2:
                self.rlt = 'あなたの負け'
            elif self.ene == 3:
                self.rlt = 'あいこ'
        else:
            print("エラーです。")
            self.pl = input("1~3を入力してください")
            return Engine.proc(self)

    def show(self):
        pl = 1
        ene = 1
        if self.pl == '1':
            pl = 'グー'
        elif self.pl == '2':
            pl = 'チョキ'
        elif self.pl == '3':
            pl = 'パー'
        if self.ene == 1:
            ene = 'グー'
        elif self.ene == 2:
            ene = 'チョキ'
        elif self.ene == 3:
            ene = 'パー'
        print('あなたは', pl, 'を出しました。')
        print('相手は', ene, 'を出しました。')
        print(self.rlt, 'です。')

    def retry(self):
        ret = input('もう一度しますか？y/n')
        if ret == 'y':
            return 
        elif ret == 'n':
            print('終了します。')
            self.ans = 'n'
            return
        else:
            print('エラーです。')
            return Engine.retry(self)

if __name__ == '__main__':
    play = Engine()
    while True:
        if play.ans == 'y':
            play.ene = random.randint(1, 3)
            play.start()
            play.proc()
            play.show()
            play.retry()
        elif play.ans == 'n':
            break
        else:
            break