from main import send_message, delete_message, load_last_message, save_last_message
from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER
from apscheduler.schedulers.background import BackgroundScheduler
import psycopg2
import os
import asyncio
import random
from apscheduler.triggers.interval import IntervalTrigger
from datetime import datetime

def save_last_run_date():
    with open("last_run_date.txt", "w") as f:
        f.write(datetime.now().strftime("%Y-%m-%d"))

def load_last_run_date():
    if os.path.exists("last_run_date.txt"):
        with open("last_run_date.txt", "r") as f:
            return f.read().strip()
    return None

def send_poems():
    last_run_date = load_last_run_date()
    today = datetime.now().strftime("%Y-%m-%d")

    if last_run_date == today:
        return
    
    db_conn = psycopg2.connect(host = DB_HOST, dbname = DB_NAME, user = DB_USER, password = DB_PASSWORD) #connecting
    db_cursor = db_conn.cursor()
    
    db_cursor.execute("SELECT COUNT (id) FROM poems") #just to know how much do we have
    poems_to_send = db_cursor.fetchall()[0][0] // 7 + 1
    
    db_cursor.execute("SELECT id FROM poems WHERE CURRENT_DATE - notification_date > 6 ORDER BY ID ASC;") 
    unsent = db_cursor.fetchall() #getting all unsent poems id
    unsent = [i[0] for i in unsent]
    unsent = random.sample(unsent, poems_to_send)
    
    for id in unsent: #date updating
        db_cursor.execute("UPDATE poems SET notification_date = CURRENT_DATE WHERE poems.id = %s", (id, ))
    db_conn.commit()
    
    text = ""
    for count, id in enumerate(unsent): #what are we gonna repeat today
        db_cursor.execute("SELECT title FROM poems WHERE poems.id = %s", (id, ))
        text += f"{count+1}. {db_cursor.fetchall()[0][0]}\n"
    text = "К повторению сегодня следующие замечательные стихи:\n\n" + text
    
    
    last_message = load_last_message()
    if last_message:
        asyncio.run(delete_message(message_id=last_message))
    last_message = asyncio.run(send_message(text=text))
    save_last_message(last_message)
    
    db_cursor.close()
    db_conn.close()
    save_last_run_date()
    pass

def start_scheduler():
    scheduler = BackgroundScheduler()

    scheduler.add_job(send_poems, IntervalTrigger(hours=3))

    scheduler.start()

    try:
        while True:
            # print("i am here and working")
            # asyncio.sleep(1)
            pass
    except (KeyboardInterrupt, SystemExit):
        send_poems()
        scheduler.shutdown()

if __name__ == "__main__":
    start_scheduler()


