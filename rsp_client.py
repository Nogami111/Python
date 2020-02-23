# rsp_client
import rsp_engine
import random

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
#ランダム数生成用のライブラリ random とジャンケン用のクラス rsp_engine をインポート
#rsp_engineをplayにインスタンス化し、
#開始(play.start)、勝敗判断(play.proc)、結果表示(play.show)、リトライ(play.retry)
#の順に処理する。
#この時リトライ引数(play.ans)の内容次第で
#もう一度繰り返させるかのループを行っている。