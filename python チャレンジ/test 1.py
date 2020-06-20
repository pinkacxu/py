import RPi.GPIO as GPIO
import time

COUNT = 5
PIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup( PIN, GPIO.OUT )

for i in range( COUNT ):
    GPIO.output( PIN, True )
    time.sleep( 1.0 )
    GPIO.output( PIN, False )
    time.sleep( 1.0 )
    GPIO.cleanup()
