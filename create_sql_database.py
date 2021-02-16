import sqlite3
import csv

conn = sqlite3.connect('languages.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS languages')
cur.execute('''
CREATE TABLE "languages"(
    "ID" TEXT,
    "title" TEXT,
    "subject_lang" TEXT,
    "year" INTEGER
)
''')

fname =input('Enter the languages csv file name: ')
if len(fname) < 1 : fname= "out.csv"

with open(fname, encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
        ID = row[0]
        title = row[1]
        subject_lang = row[2]
        year = row[3]
        cur.execute('''INSERT INTO languages(ID, title, subject_lang, year)
            VALUES (?,?,?,?)''', (ID, title, subject_lang, year))
        conn.commit()

