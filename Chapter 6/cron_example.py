from crontab import CronTab

cron = CronTab(user=True)
job = cron.new(command='cd /Users/mislam/Desktop/ml_serving_practices/Machine-Learning-Model-Serving-Patterns-and-Best-Practices/Chapter\ 6 && $(which python3) model.py')
job.minute.every(1)
# cron.remove_all() ## Command to remove all the scheduled jobs
cron.write()
