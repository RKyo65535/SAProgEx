import sqlite3

db_path = "bookdb.db"			# データベースファイル名を指定

con = sqlite3.connect(db_path)	# データベースに接続
con.row_factory = sqlite3.Row	# 属性名で値を取り出せるようにする
cur = con.cursor()				# カーソルを取得

try:
	# SQL文の実行
	cur.execute("select * from BOOKLIST where TITLE like ? and PRICE < ?", ('%JAVA%',3000,))
	rows = cur.fetchall()		# 検索結果をリストとして取得
	if not rows:				# リストが空のとき
		print("そんな本はありません")
	else:
		for row in rows:		# 検索結果を1つずつ処理

			print("ID       = %s" % str(row['ID']))
			print("タイトル = %s" % str(row['TITLE']))
			print("著者     = %s" % str(row['AUTHOR']))
			print("出版社   = %s" % str(row['PUBLISHER']))
			print("価格     = %s" % str(row['PRICE']))
			print("ISBN     = %s" % str(row['ISBN']))

			print("=============================================")#区切り棒
			
except sqlite3.Error as e:		# エラー処理
	print("Error occurred:", e.args[0])

con.commit()
con.close()
