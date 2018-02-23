import RPi.GPIO as GPIO
import time

def Main():
	LED = 19
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(LED, GPIO.OUT)

	while True:
		GPIO.output(LED, 1)
		time.sleep(0.5)
		GPIO.output(LED, 0)
		time.sleep(0.5)

if __name__ == '__main__':
    Main()