#!/usr/bin/env python3
# Refresh is working now it move to version 7
# Send Grove sensor data periodically to AWS IoT.
# Thursday afternoon final 9.13pm
# Integrating the motor code without class 16th Aug

import time
import datetime
import ssl
import json
import paho.mqtt.client as mqtt
import paho.mqtt as paho
import grovepi
from selenium import webdriver
import selenium
import json
import webbrowser
bool (True)
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)




try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import time
from grovepi import *
#import urllib.request
#from urllib.request import pathname2url


# TODO: Change this to the name of our Raspberry Pi, also known as our "Thing Name"
deviceName = "g88pi"

# Public certificate of our Raspberry Pi, as provided by AWS IoT.
deviceCertificate = "tp-iot-certificate.pem.crt"
# Private key of our Raspberry Pi, as provided by AWS IoT.
devicePrivateKey = "tp-iot-private.pem.key"
# Root certificate to authenticate AWS IoT when we connect to their server.
awsCert = "aws-iot-rootCA.crt"

isConnected = False
Like = 0  ##  Added this.  Must initialise.
tempL = 0  ##  Added this.  Must initialise.
global access_token

# Assume we connected the Grove Light Sensor to analog port A0,
# Digital Humidity/Temperature Sensor (DHT11) to digital port D2,
# Sound Sensor to A2, Grove LED to digital port D4.
# If you are using the Grove Analog Temperature Sensor, connect it to analog port A1.
light_sensor = 0      # A0 light sensor
#sound_sensor = 2
#dht_sensor = 2
led = 4 # D4
pinMode (led,"OUTPUT")
time.sleep(5)
buzzer =  8 #D8
grovepi.pinMode(buzzer,"OUTPUT")
temp_sensor = 1  # Analog temperature sensor
threshold = 450
new = 2

def get_page_data(page_id, access_token):  ##  Moved this
    global Like  ##  Added this
    # Add a random suffix to prevent caching
    random_suffix = "&random=" + datetime.datetime.now().isoformat()
    api_endpoint = "https://graph.facebook.com/v2.4/"
    fb_graph_url = api_endpoint + page_id + "?fields=id,name,likes,link&access_token=" + access_token + random_suffix
    print("fb_graph_url=" + fb_graph_url)

    try:
        api_request = urllib2.Request(fb_graph_url)
        api_response = urllib2.urlopen(api_request)

        try:
            result = api_response.read()
            result_str = str(result.decode("utf-8"))
            print(result_str)
            return json.loads(result_str)
        except (ValueError, KeyError, TypeError) as e:
            print("JSON error: " + str(e))
            return "JSON error"
    except IOError as e:
        print("IOError: " + str(e))
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason

page_id = "1318466328215016"  # username or id
token = 'EAACEdEose0cBAH3tm1hYmFZCbMqt6AIasywHRC7MvEKvks693W6XAkl0wRYOXpp8UhcR7Hqx45l5VrCkOxzcSbiwNU52dgmnBCDLB0r0Ahut5ilMsbmyP5H3UdqytCQRfA4TTpcqxOiEiWFRmZBWscmPIYgObLHfc6U6SQ3lnt4RNRZBrRl' # Access Token

#page_data = get_page_data(page_id, token)
#page_data = get_page_data(page_id, access_token)


# print ("Page Name:")+str(page_data['name'])
#print("Likes:" + str(page_data['likes']))


driver = webdriver.Firefox()
#driver.get("https://www.facebook.com/plugins/fan.php?connections=100&id=783256781810074")
driver.get("https://www.facebook.com/plugins/fan.php?connections=100&id=1318466328215016")
driver.refresh()


#webbrowser.open('https://www.facebook.com/plugins/fan.php?connections=100&id=783256781810074')

# This is the main logic of the program.  We connect to AWS IoT via MQTT, send sensor data periodically to AWS IoT,
# and handle any actuation commands received from AWS IoT.
def main():
    global isConnected
    global Like
    global tempL  ##  Added this
    # Create an MQTT client for connecting to AWS IoT via MQTT.
    client = mqtt.Client(deviceName + "_sr")  # Client ID must be unique because AWS will disconnect any duplicates.
    client.on_connect = on_connect  # When connected, call on_connect.
    client.on_message = on_message  # When message received, call on_message.
    client.on_log = on_log  # When logging debug messages, call on_log.

    # Set the certificates and private key for connecting to AWS IoT.  TLS 1.2 is mandatory for AWS IoT and is supported
    # only in Python 3.4 and later, compiled with OpenSSL 1.0.1 and later.
    client.tls_set(awsCert, deviceCertificate, devicePrivateKey, ssl.CERT_REQUIRED, ssl.PROTOCOL_TLSv1_2)

    # Connect to AWS IoT server.  Use AWS command line "aws iot describe-endpoint" to get the address.
    print("Connecting to AWS IoT...")

    client.connect("A1P01IYM2DOZA0.iot.us-west-2.amazonaws.com", 8883, 60)

    # Start a background thread to process the MQTT network commands concurrently, including auto-reconnection.
    client.loop_start()

    # Configure the Grove LED and Light port for output/ input.
    grovepi.pinMode(led, "OUTPUT")
    time.sleep(1)
    grovepi.pinMode(light_sensor,"INPUT")

    # Loop forever.
    while True:

            # If we are
        try:
            # if not connected yet to AWS IoT, wait 1 second and try again.
            if not isConnected:
                time.sleep(4)
                continue

            # check for likes
            print("Getting likes...")
            page_data = get_page_data(page_id, token)
            Like = str(page_data['likes'])
            print("Likes: " + Like)

            if int(Like) > 0  and int(Like)>  int(tempL):

                print(tempL)
                print("Inside if -success 1")
                # Buzz for 1 second
                grovepi.digitalWrite(buzzer,1)
                print ('start')
                time.sleep(3)

        # Stop buzzing for 1 second and repeat
                grovepi.digitalWrite(buzzer,0)
                print ('stop')
                time.sleep(1)
                digitalWrite(led, 1)  # Send HIGH to switch on LED
                time.sleep(10)
                digitalWrite(led, 0)  # Send HIGH to switch on LED
                tempL = Like
                GPIO.cleanup()
                GPIO.setmode(GPIO.BOARD)
                m = Motor([18,22,24,26])

                m.rpm = 5
                print("Motor start 2 0")
                m.move_to(0)
                sleep(1)
                print("Motor start 2 90")
                m.move_to(90)

                sleep(5)
                m.mode = 2
                print("Motor start 2 again 0")
                m.move_to(0)
                GPIO.cleanup()
            #elif (int(Like) = int(tempL)):
              #  #tempL = int(Like) + int(1)
                #print(tempL)
                #print("Inside if -success 2")
                #digitalWrite(led, 1)  # Send HIGH to switch on LED
                #time.sleep(10)
                #digitalWrite(led, 0)  # Send HIGH to switch on LED

            else:
                print(" not inside if -not success")
                digitalWrite(led, 0)  # Send LOW to switch off LED
                print(tempL)
                time.sleep(5)

            # Read Grove sensor values. Prepare our sensor data in JSON format.
            payload = {
                "state": {
                    "reported": {
                        # Uncomment the next line if you're using the Grove Analog Temperature Sensor.
                         "temperature": round(grovepi.temp(temp_sensor, '1.1'), 1),
                        # Comment out the next 2 lines if you're using the Grove Analog Temperature Sensor.
                       # "temperature": grovepi.dht(dht_sensor, 0)[0],  # The first 0 means that the DHT module is DHT11.
                        #####"humidity": grovepi.dht(dht_sensor, 0)[1],
                        "light_level": grovepi.analogRead(light_sensor),
                        #####"sound_level": grovepi.analogRead(sound_sensor),
                        "Likes":Like,
                        "timestamp": datetime.datetime.now().isoformat()

                    }
                }
            }

            light_value = grovepi.analogRead(light_sensor)
            print ("Light Level =",light_value)

            if threshold > light_value:
                 print("light value is low ")
                 browser = webdriver.Firefox()

                 browser.get('http://www.proprofs.com/survey/stats/?title=tm54n&shr-id=a22c0d0970ca238804d1c5e8cc270a4c&oeq=946003f97ccc52d5d3b54ac0ec31bbfc')
                 # Save the window opener (current window, do not mistaken with tab... not the same)
                 main_window = browser.current_window_handle
                 browser.maximize_window()
                 sleep(2)
                 print ('LAST STEP')
                 #browser.close() #closes new tab
                 sleep(1)
                 browser.get('http://tp-iot.weebly.com')
                 #webbrowser.get('Firefox').open('file:///home/pi/Desktop/QR.html')
                 #browser.get('file:///home/pi/Desktop/QR.html')
                 # Save the window opener (current window, do not mistaken with tab... not the same)
                 sleep (1)
                 #browser.get('Firefox').close('file:///home/pi/Desktop/QR.html')
                 browser.close() #closes new tab

            print("Sending sensor data to AWS IoT...\n" +
                  json.dumps(payload, indent=4, separators=(',', ': ')))

            # Publish our sensor data to AWS IoT via the MQTT topic, also known as updating our "Thing Shadow".
            client.publish("$aws/things/" + deviceName + "/shadow/update", json.dumps(payload))
            print("Sent to AWS IoT")
            driver.refresh()
            # Wait 30 seconds before sending the next set of sensor data.
            #schedule.run_pending()
            time.sleep(30)

        except KeyboardInterrupt:
            break
        except Exception as e:
            # For all other errors, we wait a while and resume.
            print("Exception: " + str(e))
            time.sleep(10)
            continue

# This is called when we are connected to AWS IoT via MQTT.
# We subscribe for notifications of desired state updates.
def on_connect(client, userdata, flags, rc):
    global isConnected
    isConnected = True
    print("Connected to AWS IoT")
    # Subscribe to our MQTT topic so that we will receive notifications of updates.
    topic = "$aws/things/" + deviceName + "/shadow/update/accepted"
    print("Subscribing to MQTT topic " + topic)
    client.subscribe(topic)
    #driver = webdriver.Firefox()
    #driver.get("https://www.facebook.com/plugins/fan.php?connections=100&id=783256781810074")
    driver.refresh()

# This is called when we receive a subscription notification from AWS IoT.
def on_message(client, userdata, msg):
    # Convert the JSON payload to a Python dictionary.
    # The payload is in binary format so we need to decode as UTF-8.
    payload2 = json.loads(msg.payload.decode("utf-8"))
    print("Received message, topic: " + msg.topic + ", payload:\n" +
          json.dumps(payload2, indent=4, separators=(',', ': ')))


# Print out log messages for tracing.
def on_log(client, userdata, level, buf):
    print("Log: " + buf)

# Stepper MOTOR CODE PART

class Motor(object):
    def __init__(self, pins, mode=3):
        """Initialise the motor object.

        pins -- a list of 4 integers referring to the GPIO pins that the IN1, IN2
                IN3 and IN4 pins of the ULN2003 board are wired to
        mode -- the stepping mode to use:
                1: wave drive (not yet implemented)
                2: full step drive
                3: half step drive (default)

        """
        self.P1 = pins[0]
        self.P2 = pins[1]
        self.P3 = pins[2]
        self.P4 = pins[3]
        self.mode = mode
        self.deg_per_step = 5.625 / 64  # for half-step drive (mode 3)
        self.steps_per_rev = int(360 / self.deg_per_step)  # 4096
        self.step_angle = 0  # Assume the way it is pointing is zero degrees
        for p in pins:
            GPIO.setup(p, GPIO.OUT)
            GPIO.output(p, 0)


    def _set_rpm(self, rpm):
        """Set the turn speed in RPM."""
        self._rpm = rpm
        # T is the amount of time to stop between signals
        self._T = (60.0 / rpm) / self.steps_per_rev

    # This means you can set "rpm" as if it is an attribute and
    # behind the scenes it sets the _T attribute
    rpm = property(lambda self: self._rpm, _set_rpm)

    def move_to(self, angle):
        """Take the shortest route to a particular angle (degrees)."""
        # Make sure there is a 1:1 mapping between angle and stepper angle
        target_step_angle = 8 * (int(angle / self.deg_per_step) / 8)
        steps = target_step_angle - self.step_angle
        steps = (steps % self.steps_per_rev)
        if steps > self.steps_per_rev / 2:
            steps -= self.steps_per_rev
            #print "moving " + `steps` + " steps"
            if self.mode == 2:
                self._move_acw_2(-steps / 8)
            else:
                self._move_acw_3(-steps / 8)
        else:
            #print "moving " + `steps` + " steps"
            if self.mode == 2:
                self._move_cw_2(steps / 8)
            else:
                self._move_cw_3(steps / 8)
        self.step_angle = target_step_angle

    def __clear(self):
        GPIO.output(self.P1, 0)
        GPIO.output(self.P2, 0)
        GPIO.output(self.P3, 0)
        GPIO.output(self.P4, 0)

    def _move_acw_2(self, big_steps):
        self.__clear()
        for i in range(big_steps):
            GPIO.output(self.P3, 0)
            GPIO.output(self.P1, 1)
            sleep(self._T * 2)
            GPIO.output(self.P2, 0)
            GPIO.output(self.P4, 1)
            sleep(self._T * 2)
            GPIO.output(self.P1, 0)
            GPIO.output(self.P3, 1)
            sleep(self._T * 2)
            GPIO.output(self.P4, 0)
            GPIO.output(self.P2, 1)
            sleep(self._T * 2)

    def _move_cw_2(self, big_steps):
        self.__clear()
        for i in range(big_steps):
            GPIO.output(self.P4, 0)
            GPIO.output(self.P2, 1)
            sleep(self._T * 2)
            GPIO.output(self.P1, 0)
            GPIO.output(self.P3, 1)
            sleep(self._T * 2)
            GPIO.output(self.P2, 0)
            GPIO.output(self.P4, 1)
            sleep(self._T * 2)
            GPIO.output(self.P3, 0)
            GPIO.output(self.P1, 1)
            sleep(self._T * 2)

    def _move_acw_3(self, big_steps):
        self.__clear()
        for i in range(big_steps):
            GPIO.output(self.P1, 0)
            sleep(self._T)
            GPIO.output(self.P3, 1)
            sleep(self._T)
            GPIO.output(self.P4, 0)
            sleep(self._T)
            GPIO.output(self.P2, 1)
            sleep(self._T)
            GPIO.output(self.P3, 0)
            sleep(self._T)
            GPIO.output(self.P1, 1)
            sleep(self._T)
            GPIO.output(self.P2, 0)
            sleep(self._T)
            GPIO.output(self.P4, 1)
            sleep(self._T)

    def _move_cw_3(self, big_steps):
        self.__clear()
        for i in range(big_steps):
            GPIO.output(self.P3, 0)
            sleep(self._T)
            GPIO.output(self.P1, 1)
            sleep(self._T)
            GPIO.output(self.P4, 0)
            sleep(self._T)
            GPIO.output(self.P2, 1)
            sleep(self._T)
            GPIO.output(self.P1, 0)
            sleep(self._T)
            GPIO.output(self.P3, 1)
            sleep(self._T)
            GPIO.output(self.P2, 0)
            sleep(self._T)
            GPIO.output(self.P4, 1)
            sleep(self._T)



if __name__ == "__main__":

        GPIO.setmode(GPIO.BOARD)
        m = Motor([18,22,24,26])

        m.rpm = 5
        #print "Pause in seconds: " + `m._T`
        print("Motor start")
        m.move_to(0)
        sleep(1)
        m.move_to(90)
        sleep(5)
        m.mode = 2
        m.move_to(0)
        print("Motor end")
        GPIO.cleanup()
        main ()
