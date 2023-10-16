import schedule
import time

# Functions setup


def job1():
    print("Job1 is running...")


def job2():
    print("Job2 is running...")


def job3():
    print("Job3 is running...")


def job4():
    print("Job4 is running...")


def job5():
    print("Job5 is running...")


# Task scheduling
# After every 5 mins
schedule.every(5).minutes.do(job1)

# After every hour
schedule.every().hour.do(job2)

# Every day at 12am or 00:00 time.
schedule.every().day.at("00:00").do(job3)

# After every 5 to 10 mins.
schedule.every(5).to(10).minutes.do(job4)

# Every sunday
schedule.every().sunday.do(job5)

# Every sunday at 18:00 sudo_placement() is called
schedule.every().tuesday.at("13:00").do(job1)

# Loop so that the scheduling task
# keeps on running all time.
while True:

    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
