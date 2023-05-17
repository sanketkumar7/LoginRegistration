from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from .views import myfunction

scheduler = BackgroundScheduler()
def scheduled_function():
    myfunction()
scheduler.add_job(scheduled_function, 'cron', hour=17)
scheduler.start()

