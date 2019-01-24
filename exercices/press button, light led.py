import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)
GPIO.add_event_detect(4, GPIO.BOTH)
def my_callback():
    GPIO.output(25, GPIO.input(4))
    print('PUSHED!')
GPIO.add_event_callback(4, my_callback)
