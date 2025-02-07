from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(schedule, 'interval', hours=24)
    scheduler.start()
