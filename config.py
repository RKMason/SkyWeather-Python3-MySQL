
#
#
# Baseline configuration file - contains customization for SkyWeather system
#
# It is a good idea to copy this file into a file called "conflocal.py" and edit that instead of this one.
#
# This file is wiped out if you update SkyWeather.

#Debugmodes
SWDEBUG = False
DEBUGBLYNK = False
MySQL_debug = False
WU_debug = False
AS3935_debug = False
#END
#check for git

# Set from SkyWeather.Py startup
SWVERSION = "000" 
#END

#MAIL
mailUser = "yourusename"
mailPassword = "yourmailpassword"
notifyAddress ="you@example.com"
fromAddress = "yourfromaddress@example.com"
enableText = False
textnotifyAddress = "yourphonenumber@yourprovider"


#MySQL Logging and Password Information
enable_MySQL_Logging = True
MySQL_Password = ""


# modify this IP to enable WLAN operating detection  - search for WLAN_check in SkyWeather.py
enable_WLAN_Detection = False
PingableRouterAddress = "192.168.1.1"

# LED configuration (on use on a Raspberry Pi 3B+)
runLEDs = False

# WXLink and SolarMAX configuration
SolarMAX_Present = False
Dual_MAX_WXLink = False

# SolarMAX_Type = "LEAD" for SolarMAX Lead Acid
# SolarMAX_Type = "LIPO" for SolarMAX LiPo
SolarMAX_Type = ""

# WeatherSTEM configuration
USEWEATHERSTEM = False
INTERVAL_CAM_PICS__SECONDS = 60
STATIONMAC = ""
STATIONKEY="XXXXYYYY"
STATIONHARDWARE=""


# WeatherUnderground Station
WeatherUnderground_Present = True
WeatherUnderground_StationID = "YourStationID"
WeatherUnderground_StationKey = "YourStationKey"


# Blynk configuration
USEBLYNK = False 
BLYNK_AUTH = 'xxxxx'
BLYNK_URL = 'http://blynk-cloud.com/'


# AS3935 Lightning Configuration
# format: [NoiseFLoor, Indoor, TuneCap, DisturberDetection, WatchDogThreshold, SpikeDetection]
AS3935_Lightning_Config = [2,1,3,0,3,3]



# for barometeric pressure - needed to calculate sealevel equivalent - set your weatherstation elevation here
BMP280_Altitude_Meters = 242.0  #Set this to your location

# Device present global variables. Adjust for your own hardware config.

Camera_Present = False
TCA9545_I2CMux_Present = True
SunAirPlus_Present = False
AS3935_Present = False
DS3231_Present = False
BMP280_Present = False
BME680_Present = True
HDC1080_Present = False
SHT30_Present = True
AM2315_Present = False
ADS1015_Present = True
ADS1115_Present = False
OLED_Present = True
OLED_Originally_Present = True
WXLink_Present = False
Sunlight_Present = False
TSL2591_Present = False
MP503_Present = False
WatchDog_Present = False

#set this to true if you have the sensor, false if you do not
DustSensor_Present = False

# set Sunlight High Gain (indoors - 1) or Low Gain (outdoors - 0)
Sunlight_Gain = 0


# if the WXLink has stopped transmitting, == False
WXLink_Data_Fresh = False
WXLink_LastMessageID = 0

# Pin definitions
pixelPin = 21

#Dust Sensor
DustSensorPin = 19
DustSensorPowerPin = 26

#WeatherRack 
anemometerPin = 20
rainPin = 13

#Temperature sensor
SHT30GSPIN = 6
AM2315GSPIN = 6

# for fan
GPIO_Pin_PowerDrive_Sig1 = 5
GPIO_Pin_PowerDrive_Sig2 = 5     # To avoid stepping on GPIO 6 

#Watchdog
WATCHDOGTRIGGER = 4

#offsets
TempOffset = 0 #in Celcius
HumOffset = 0
