#! /usr/bin/env python3

import sys
import io
import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')



print("Content-type: text/html\n")
print("<html>")
print("  <head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/></head>")
print("  <body>")
print("  SAプロ演の時刻を表示する課題ですよ<br>")
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

print("  </body>")

print("</html>")