import csv
import csv
import sqlite3


db_path = "bookdb.db"# データベースファイル名を指定

con = sqlite3.connect(db_path)	# データベースに接続
cur = con.cursor()				# カーソルを取得

try:
    cur.execute("create table BOOKLIST(ID int primary key,AUTHOR varchar(256),TITLE varchar(512),PUBLISHER varchar(256),PRICE int,ISBN char(10))")#データベースの作成
    
except sqlite3.Error as e:		# エラー処理
	print("Error occurred:", e.args[0])


with open('./BookList_sjis.csv', 'r') as file:# CSVファイルをオープン
		reader = csv.reader(file)
		for line in reader:						# 一行ずつ読み込む
			# INSERT INTO文の実行
			cur.execute('insert into BOOKLIST values (?,?,?,?,?,?);', line)#タプルであるline(要素6こ)を、AQL文として渡す


con.commit()					# データベース更新の確定
con.close()						# データベースを閉じる


