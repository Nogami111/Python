# rsp_client
"""
ジャンケンを行うためのモジュールです。
ジャンケンの各処理を行うための
<rsp_engine>と
ランダム数を生成するための
<random>モジュールをインポートしてます。
"""

import rsp_engine
import random
"""
    
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

play = rsp_engine.Engine()


while True:
    if play.ans == 'y':
        play.ene = random.randint(1, 3)
        print("グーなら1、チョキなら２、パーなら３を入力してください\n勝ち負け引き分けの結果が出力されます\n123以外の入力がされた場合にはエラーが出力されます")
        play.pl = input("1~3を入力してください")
        play.proc()
        play.show()
        play.ans = input('もう一度しますか？y/n')
    elif play.ans == 'n':
        print('終了します。')
        play.ans = 'n'
        break
    else:
        print('エラーです。')
        play.ans = input('もう一度しますか？y/n')