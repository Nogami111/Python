# RSP_engine

"""
ジャンケンの処理を行うためのモジュールです。
"""

import random

class Engine:
    """
    ジャンケン用のクラスです。
    
    self.pl<str>:
    プレイヤーの出した手を表す引数です。
    plはplayerを意味します。
    1〜３を入力します。
    この入力した数字でグー(1)、チョキ(2)、パー(3)
    を判断します。

    self.ene<int>:
    相手の出す手を表す引数です。
    eneはenemyを意味します。
    randomモジュールのrandintによって
    1~3がランダムに初期値として代入されます。
    こちらで代入された1~3の値でジャンケンの勝敗を判断します。

    self.rlt<str>:
    ジャンケンの結果を表す引数です。
    rltはresultを意味します。
    初期値には''が代入されていますが
    ジャンケンの勝敗が判断された後に
    'あなたの勝ち'、'あなたの負け'、'あいこ'
    が代入されます。
    ここで代入されたものが結果表示の際に使用されます。

    self.ans<str>:
    リトライするかどうかを表す引数です。
    ansはanswerを意味します。
    初期値には'y'が代入されています。
    'y'がはい、'n'がいいえ
    を表します。
    ここで代入されたもので、再度ジャンケンを行うか否かを判断します。
    """
    def __init__(self, pl='0', ene=random.randint(1, 3), rlt='', ans='y'):
        self.pl = pl
        self.ene = ene
        self.rlt = rlt
        self.ans = ans


    def start(self):
        """
        ジャンケンを始めるための関数です。
        startはそのままstartを意味します。
        1~3の引数を入力させ,<self.pl>に格納します。
        ここではその他の文字が入力された場合の処理はしません。
        """
        print("グーなら1、チョキなら２、パーなら３を入力してください\n勝ち負け引き分けの結果が出力されます\n123以外の入力がされた場合にはエラーが出力されます")
        self.pl = input("1~3を入力してください")

    def proc(self):
        """
        ジャンケンの勝敗の判断をする関数です。
        procはprocessing(処理)を意味します。
        入力された<self.pl>と
        生成された<self.ene>で
        ジャンケンの勝敗を判断します。
        ここで出た結果は<self.rlt>に格納されます。
        また、格納されている<self.pl>が1~3以外の場合、
        'エラーです'の表示と、
        再度1~3の引数を入力させる処理が行われます。
        入力後、returnで再度この関数の処理に返します。
        """
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
        """
        ジャンケン結果を表示する関数です。

        pl<str>:
        <self.pl>に格納された1~3の値を
        それぞれグー、チョキ、パー
        に変えるための変数です。
        ここで格納された値は
        プレイヤーの出した手の表示に使用します。

        ene<str>:
        <self.ene>に格納された1~3の値を
        それぞれグー、チョキ、パー
        に変えるための変数です。
        ここで格納された値は
        相手の出した手の表示に使用します。

        <self.pl>及び<self.ene>に格納されている値を
        'グー'、'チョキ'、'パー'の表記に変え、
        <pl>、<ene>に格納します。
        結果の表示には<self.rlt>に格納されている値を使用します。
        """
        pl = ''
        ene = ''
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
        """
        もう一度ジャンケンを行うかを判断する関数です。

        ret<str>:
        もう一度ジャンケンを行うかを判断するのに使用する変数です。
        'y'、'n'、その他の値で判断を行います。

        ここで'y'が入力された場合は
        戻り値なしのreturnを返します。
        ここで'n'が入力された場合は
        終了します。の表示を行い、
        <self.ans>に'n'を格納します。
        ここでその他の値が入力された場合は
        エラーです。の表示を行い、
        returnで再度この関数の処理に返します。
        """
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
    """
    テスト用の処理です。
    
    play<str>:
    クラス<Engine>を<play>インスタンス化します。

    whileはtrueの場合にループを行います。
    falseの時の処理はないです。

    <play.ans>の値が'y'の場合は
    ジャンケンの各処理を行います。
    リトライをした時のためにここで
    <randint>により1~3をランダム生成し、
    play.eneに格納します。

    <play.ans>の値が'n'の場合は
    breakします。

    <play.ans>の値がその他の場合でも
    breakします。
    """
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