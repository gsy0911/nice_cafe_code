from utils import random_sleep


def dung_status_change(sharp_num=50):
    """
    > ステータスが変化してる風コード
    """
    counter = 0
    while True:
        if counter < sharp_num:
            print("#", end="", flush=True)
        else:
            print(" done!!")
            counter = -1
        counter += 1
        random_sleep(0.01, 0.1)


if __name__ == "__main__":
    dung_status_change()
