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
        play.start()
        play.proc()
        play.show()
        play.retry()
    elif play.ans == 'n':
        break
    else:
        break