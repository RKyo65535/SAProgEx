#! /usr/bin/env python3

import sys
import io
import cgi
import sqlite3

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()
searchWord = form.getvalue('searchWord','No Input')


print("Content-type: text/html\n")
print("<html>")
print("  <head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/></head>")
print("  <body>")

#printf(searchWord)これを表示しようとするとエラーになる

db_path = "DataBase/bookdb.db"			# データベースファイル名を指定

con = sqlite3.connect(db_path)	# データベースに接続
con.row_factory = sqlite3.Row	# 属性名で値を取り出せるようにする
cur = con.cursor()				# カーソルを取得

try:
	# SQL文の実行
	cur.execute("select * from BOOKLIST where TITLE like ? or AUTHOR like ?", ("%"+searchWord+"%","%"+searchWord+"%"))
	rows = cur.fetchall()		# 検索結果をリストとして取得
	if not rows:				# リストが空のとき
		print("そんな本はありません")
	else:
		print("「")
		print(searchWord)
		print("」")
		print("で検索した結果、")

		print("見つかった本は以下の通りです<p>")
		print("=============================================<p>")#区切り棒

		for row in rows:		# 検索結果を1つずつ処理

			print("ID       = %s<br>" % str(row['ID']))
			print("タイトル = %s<br>" % str(row['TITLE']))
			print("著者     = %s<br>" % str(row['AUTHOR']))
			print("出版社   = %s<br>" % str(row['PUBLISHER']))
			print("価格     = %s<br>" % str(row['PRICE']))
			print("ISBN     = %s<p>" % str(row['ISBN']))

			print("=============================================<p>")#区切り棒
			
except sqlite3.Error as e:		# エラー処理
	print("Error occurred:", e.args[0])

con.commit()
con.close()

print("  </body>")

print("</html>")