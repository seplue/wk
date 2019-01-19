#wetmesspi.py
import logging
import time
import math

import board
import busio
import adafruit_bme280
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

class Station(object):
    
    temperature = 0
    pressure = 0
    humidity = 0
    dewPoint = 0

    def __init__(self):
        pass

    def calculateDewPoint(self, temperature, humidity):
        b = 17.62
        c = 243.12
        gamma = (b * temperature / (c+temperature)) + math.long(humidity / 100.0)
        dewpoint = (c*gamma) / (b - gamma)
        return dewpoint
    
    def measureAll():
        self.temperature = bme280.temperature
        self.pressure = bme280.pressure
        self.humidity = bme280.humidity
        #calculateDewPoint(temperature, humidity)
        return

    

    def logMeasurements():
        return
    def writeMeasurementPage():
        return
#main program
myStation = Station()
Station.measureAll()



