import RPi.GPIO as GPIO
import sys,time,signal,os
import subprocess

from myutils import contains,cleanup,sysout

# 25からはじまりGNDへ落ちる回路を組む。
# これは物理的な配置番号ではなく、GPIO の番号。
sw_pin = 25

#cf. http://mamerium.com/raspberry-pi-rpi-gpio-basic/


def main(args):
	signal.signal(signal.SIGINT, cleanup)
	signal.signal(signal.SIGTERM, cleanup)

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(sw_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	interval = 0.02
	counter = 0
	try:
		while True:
			#押した直後なのでゼロかな
			state = GPIO.input(sw_pin)
			# 押しているときはゼロ.1のときは、で分岐。
			if(not(state)):
				print("Switchの状態",not(state))
				counter += 1
				# 3秒おしぱなしだったら。
				if(counter > 100):
					shutdownMessage = 'shutdownします'
					# speak( shutdownMessage )
					time.sleep(1)
					sysout(shutdownMessage)
					subprocess.call('sudo shutdown -h now',shell=True)
					counter = 0
			else:
				print("Switchの状態",not(state))
				counter = 0
				# 押されるまで、まち？
				GPIO.wait_for_edge(sw_pin, GPIO.FALLING, timeout=2000)
			print("Counter: ",counter)
			time.sleep(interval)
			sys.stdout.flush()

	except Exception as e:
		raise
	finally:
		sysout("clean up")
		GPIO.cleanup()


if __name__ == '__main__':
	# http://www.python-izm.com/contents/basis/command_line_arguments.shtml
	# sysout(args[0])
	# sysout(args[1]) でアクセス出来るが、args[0]はプログラム名。
	main(sys.argv)
