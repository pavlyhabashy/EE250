import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import time

def Main()
	LED = 12
	GPIO.setup(LED, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(LED, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	while True:
		GPIO.output(LED, 1)
		time.sleep(0.5)
		GPIO.output(LED, 0)
		time.sleep(0.5)

if __name__ == '__main__':
    Main()