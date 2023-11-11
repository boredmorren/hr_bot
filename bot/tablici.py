import sqlite3 as sq

con = sq.connect('oprosniki2.db')

cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
            id_user INTEGER PRIMARY KEY AUTOINCREMENT,
            tg_id TEXT,
            user_fullname TEXT,
            id_inc TEXT,
            user_job TEXT);
""")
con.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Survey(
            id_survey INTEGER PRIMARY KEY AUTOINCREMENT,
            survey_name TEXT);
""")
con.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Questions(
            id_survey INTEGER,
            id_question INTEGER PRIMARY KEY AUTOINCREMENT,
            question_text TEXT,
            FOREIGN KEY(id_survey) REFERENCES Survey(id_survey));
""")
con.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Answers(
            id_question INTEGER,
            id_answer INTEGER PRIMARY KEY AUTOINCREMENT,
            answer_text TEXT,
            FOREIGN KEY(id_question) REFERENCES Questions(id_question));
""")
con.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS User_answer(
            id_user INTEGER,
            id_survey INTEGER,
            answers TEXT,
            FOREIGN KEY(id_user) REFERENCES users(id_user),
            FOREIGN KEY(id_survey) REFERENCES Survey(id_survey));
""")
con.commit()