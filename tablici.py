import sqlite3 as sq

con = sq.connect('oprosniki2.db')

cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
            id_inc TEXT,
            id_user INTEGER PRIMARY KEY,
            user_fullname TEXT,
            tg_url TEXT,
            user_job TEXT);
""")
con.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Survey(
            id_survey INTEGER PRIMARY KEY,
            survey_name TEXT);
""")
con.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Questions(
            id_servey INTEGER,
            id_question INTEGER PRIMARY KEY,
            question_text TEXT,
            FOREIGN KEY(id_servey) REFERENCES Survey(id_survey));
""")
con.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Answers(
            id_questions INTEGER,
            id_answer INTEGER PRIMARY KEY,
            answer_text TEXT,
            FOREIGN KEY(id_questions) REFERENCES Questions(id_question));
""")
con.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS User_answer(
            id_usera INTEGER,
            id_survevey INTEGER,
            answers TEXT,
            FOREIGN KEY(id_usera) REFERENCES users(id_user),
            FOREIGN KEY(id_survevey) REFERENCES Survey(id_survey));
""")
con.commit()