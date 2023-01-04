import datetime
from settings.variables import my_choice

# FUNCTIONS
def countdown(m):
    total_seconds = m * 60
    return total_seconds

def convert(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)

def write_choice():
    # TEXT FILE FOR LOGS
    with open("source/text/log.txt", mode="a") as file:
        time = datetime.datetime.now()
        file.write(my_choice + '  ' + time.strftime("%d.%B %H:%M") + "\n")

