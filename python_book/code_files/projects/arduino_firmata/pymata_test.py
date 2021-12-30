"""
file: pymata_test.py
author: Mark Redd
about:
Simple test of the pymata_aio package for interacting with arduino.
"""

from pymata_aio.pymata3 import PyMata3 as pfm
from pymata_aio.constants import Constants as c


def blink_10_times():
    board = pfm()
    board.set_pin_mode(13, c.OUTPUT)
    for i in range(10):
        board.digital_write(13, 1)
        board.sleep(0.5)
        board.digital_write(13, 0)
        board.sleep(0.5)
        print(board.analog_read(0))

    board.shutdown()


if __name__ == "__main__":
    blink_10_times()
