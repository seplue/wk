import RPi.GPIO as GPIO
import time as time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

f = open("humidityStateChanges_log.txt", "a")
f.write("File opened\n")
oldHumidityState = GPIO.input(4)
if(oldHumidityState == 0):
    print("The soil is wet")
    f.write("The soil is wet\n")
else:
    print("The soil is dry")
    f.write("The soil is dry\n")

    

while(True):
    newHumidityState = GPIO.input(4)


    if(oldHumidityState != newHumidityState):
        if(newHumidityState == 0):
            print("The soil is wet")
            f.write("The soil is wet\n")
        else:
            print("The soil is dry")
            f.write("The soil is dry\n")


        
    oldHumidityState = newHumidityState
    time.sleep(1)
