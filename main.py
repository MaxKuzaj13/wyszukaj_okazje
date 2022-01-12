from grab_from_olx import scrap_data
import schedule
import time
import json


def job():
    print("I'm working...")
    scrap_data()

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)