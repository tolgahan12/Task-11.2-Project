#!/usr/bin/env python
 
from GmailWrapper import GmailWrapper
 
import RPi.GPIO as GPIO
import time
 
HOSTNAME = 'imap.gmail.com'
USERNAME = '<your gmail username>'
PASSWORD = '<your app password or regular gmail password>'
 
def feedByGmail():
    gmailWrapper = GmailWrapper(HOSTNAME, USERNAME, PASSWORD)
    ids = gmailWrapper.getIdsBySubject('feed cats')
    if(len(ids) > 0):
        try:
            feed()
            gmailWrapper.markAsRead(ids)
        except:
            print("Failed to feed cats, they're starvingggg")
 
def feed():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
 
    try:
        servo = GPIO.PWM(18, 50)
        servo.start(12.5)
 
        for index in range(0, 3):
            dutyCycle = 2.5 if (index % 2 == 0) else 12.5
            servo.ChangeDutyCycle(dutyCycle)
            time.sleep(0.8)
    finally:
        servo.stop()
        GPIO.cleanup()
 
if __name__ == '__main__':
    feedByGmail()
