This is the initial commit of a fork off of the "ve3sjk/SkyWeather-Python-3" port of SkyWeather to Python 3

NOTE: Just as ve3sjk said, this is a work in progress. The "ve3sjk/SkyWeather-Python-3" Python 3 port supports
the following list of sensors. My effort here was focussed on reverting the ve3sjk Python 3 code back to use of SwitchDoc
Labs original MySQL database code. My system also includes the PiWeatherboard V1.1 using a TCA9545 I2C Mux so Python 3 
support for it is included. 

 The Python 3 port by ve3sjk supports the following list of sensors. My SkyWeather hardware system uses a subset of
 this sensor list as marked by a * (plus I added Python3 support for the TCA9545 I2C Mux) .  

- Currently operating with these sensors:

- as3935
- veml6070
- bme680*
- sht30*
- ads1015*
- oled* (hardware attached but not currently working correctly)
- tsl2591
- weatherack*
- tca9545* 

- Python 3 system is now reverted back to using the original MySQL db.

- Sending weather data to WeatherUnderground is verified by me.
- The other alternative weather data upload options have not been modified by me. 

- Two new "device-Present =" config file switches added:
 
- "MP503_Present = "
- "WatchDog_Present = "

- Removed these now unused settings in config file

- MySQL_Address = "x.x.x.x"
- MySQL_User = "xxxx"
- MySQL_Database = "xxxx"
- MySQL_Database2 = "xxxx"

- I am running SkyWeather under PiOS "Bullseye" on a RPi Zero W.

- To setup your PiOS follow the GitHub "switchdoclabs/SDL_Pi_SkyWeather" Readme instructions, but instead install Python 3
- versions of each of the PiOS Python support utilities (typically named "Python3-xxxx"). When installing the Adafruit Python
- device utilities you will see warnings about using deprecated install processes, but the install processes did work.
- Obviously, you should git clone this SkyWeather-Python3-MySQL repository instead of the original SDL version. 

 

- The info below is from ve3sjk. I have not yet tried running SkyWeather as a background service.

*******************************************************************************************************
Getting it to run as a background service

 - change to pigpio-develop directory 
 - run make
 - run make install
 
 This will install the development verison
 of pigpio that is currently working on my
 develpment system which is raspberry Pi4b
 running Ubuntu Server 20.04 via direct USB
 boot from external SSD.
 
 create a cron job, i use webmin for this
 on the server that runs startserver.sh
 in the root directory at boot
 
 
 all the original version can be found below.
 
 
SkyWeather Libraries and Examples for Raspberry Pi Solar Powered Weather Station<BR>

Supports SwitchDoc Labs WeatherRack PiWeather Board <BR> 

All documentation is on:<BR>

https://shop.switchdoc.com/products/skyweather-raspberry-pi-based-weather-station-kit-for-the-cloud

December 15, 2019: Version 055 - MySQL SolarMAX Fixes

*******************************************************************************************************

