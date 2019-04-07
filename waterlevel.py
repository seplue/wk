#waterlevel.py

import RPi.GPIO as GPIO
import logging
import time
import math

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)





while True:
    state0 = GPIO.input(15)
    print("The state is: %s" %state0)
    time.sleep(1)

