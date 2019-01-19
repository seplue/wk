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
    
    def measureAll(self):
        self.temperature = bme280.temperature
        self.pressure = bme280.pressure
        self.humidity = bme280.humidity
        self.dewPoint = self.temperature - ((100 - self.humidity) / 5)

    def printAll(self):
        print("temperature: ", self.temperature)
        print("pressure: ", self.pressure)
        print("humidity: ", self.humidity)
        print("dewPoint: ", self.dewPoint)
    def logMeasurements():
        return
    def writeMeasurementPage():
        return



#main program
myStation = Station()
myStation.measureAll()
myStation.printAll()
