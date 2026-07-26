import ntptime
import time


def sync_time():

    try:

        print("Updating clock...")

        ntptime.settime()

        print("Time updated:")
        print(time.localtime())

        return True


    except Exception as e:

        print("Clock update failed")
        print(e)

        return False