ラズパイで動くシリアルデータチェックプログラム  
　Raspberry-Pi のシリアルポートに 0x00-0xff の循環データを入力し、正しく受信できているかをチェックする

※このプログラムが起動してから、データ送出を開始すること

serial-data-checker.py &lt;speed&gt;  
  シリアルポートから入力されたデータが 0x00-0xff の循環データかチェックす。結果は、データの入力が無くなった５秒後にターミナルに表示される。

開発環境

Raspberry Pi B

pi@raspberrypi:~/sdg $ uname -a  
Linux raspberrypi 4.4.21+ #911 Thu Sep 15 14:17:52 BST 2016 armv6l GNU/Linux

pi@raspberrypi:~/sdg $ python --version  
Python 2.7.9

OS への変更点はこちらを参照  
http://qiita.com/ryugyoku/items/bf5fd10512c84a55d030
