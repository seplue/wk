[1mdiff --git a/.idea/deployment.xml b/.idea/deployment.xml[m
[1mindex e08def6..767509d 100644[m
[1m--- a/.idea/deployment.xml[m
[1m+++ b/.idea/deployment.xml[m
[36m@@ -1,6 +1,6 @@[m
 <?xml version="1.0" encoding="UTF-8"?>[m
 <project version="4">[m
[31m-  <component name="PublishConfigData">[m
[32m+[m[32m  <component name="PublishConfigData" autoUpload="Always" serverName="pi@192.168.1.31:22">[m
     <serverData>[m
       <paths name="pi@192.168.1.31:22">[m
         <serverdata>[m
[36m@@ -10,5 +10,6 @@[m
         </serverdata>[m
       </paths>[m
     </serverData>[m
[32m+[m[32m    <option name="myAutoUpload" value="ALWAYS" />[m
   </component>[m
 </project>[m
\ No newline at end of file[m
[1mdiff --git a/station.py b/station.py[m
[1mindex 6b316a0..f439c8d 100644[m
[1m--- a/station.py[m
[1m+++ b/station.py[m
[36m@@ -11,6 +11,7 @@[m [mimport adafruit_bme280[m
 i2c = busio.I2C(board.SCL, board.SDA)[m
 bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)[m
 [m
[32m+[m
 class Station(object):[m
     [m
     temperature = 0[m
[36m@@ -38,6 +39,7 @@[m [mclass Station(object):[m
         print("humidity: ", self.humidity)[m
         print("dewPoint: ", self.dewPoint)[m
         print("----------------------------")[m
[32m+[m
     def logMeasurement(self):[m
         logging.info("time: " + self.measurementTime + "\n")[m
         logging.info("temperature: " + str(self.temperature) + "\n")[m
[36m@@ -46,6 +48,7 @@[m [mclass Station(object):[m
         logging.info("dewPoint: " + str(self.dewPoint) + "\n")[m
         logging.info("----------------------------\n")[m
         return[m
[32m+[m
     def writeMeasurementPage(self):[m
         f = open("/var/www/html/wk/lastMeasurement.txt", "w")[m
         f.write("time: " + self.measurementTime + "\n")[m
[36m@@ -56,6 +59,7 @@[m [mclass Station(object):[m
         f.write("----------------------------\n")[m
         f.close()[m
         return[m
[32m+[m
     def continuousWork(self):[m
         while True:[m
             self.measureAll()[m
