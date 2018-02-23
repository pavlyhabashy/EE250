import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import time

def Main()
	while True:
		GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		time.sleep(0.5)
		GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		time.sleep(0.5)

if __name__ == '__main__':
    Main()