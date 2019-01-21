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
        self.measurementTime = time.asctime()
        self.temperature = bme280.temperature
        self.pressure = bme280.pressure
        self.humidity = bme280.humidity
        self.dewPoint = self.temperature - ((100 - self.humidity) / 5)

    def printAll(self):
        print("time: ", self.measurementTime)
        print("temperature: ", self.temperature)
        print("pressure: ", self.pressure)
        print("humidity: ", self.humidity)
        print("dewPoint: ", self.dewPoint)
        print("----------------------------")
    def logMeasurements():
        return
    def writeMeasurementPage(self):
        f = open("/var/www/html/wk/lastMeasurement.txt", "w")
        f.write("time: " + self.measurementTime + "\n")
        f.write("temperature: " + str(self.temperature) + "\n")
        f.write("pressure: " + str(self.pressure) + "\n")
        f.write("humidity: " + str(self.humidity) + "\n")
        f.write("dewPoint: " + str(self.dewPoint) + "\n")
        f.write("----------------------------\n")
        f.close()
        return
    def continuousWrite(self):
        while True:
            self.measureAll()
            self.writeMeasurementPage()
            self.printAll()
            time.sleep(5)
        return


#main program
myStation = Station()
#myStation.measureAll()
#myStation.printAll()
#myStation.writeMeasurementPage()
myStation.continuousWrite()
