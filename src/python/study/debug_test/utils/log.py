import datetime

def log(message):
    dt_now = datetime.datetime.now()
    print(str(dt_now) + ": " + str(message))