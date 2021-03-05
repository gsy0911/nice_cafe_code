from random import random
from utils import random_sleep


def dung_compiler(code_num=50):
    """
    > コンパイルが動いている風コード
    """
    while True:
        print("".join([str(int(random()*10)) for _ in range(code_num)]))
        random_sleep(0.1, 0.5)


if __name__ == "__main__":
    dung_compiler()
