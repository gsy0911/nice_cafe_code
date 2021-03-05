from time import sleep
from random import random


def random_sleep(short_sleep, long_sleep):
    """
    適当な秒数待つ関数
    """
    r = int(random() * 10)
    sleep_time = long_sleep if (4 < r <= 6) else short_sleep
    sleep(sleep_time)
