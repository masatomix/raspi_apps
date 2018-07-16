import RPi.GPIO as GPIO
import sys, time, signal, os
import subprocess

from myutils import contains,speak,cleanup, sysout

# 25からはじまりGNDへ落ちる回路を組む。
# これは物理的な配置番号ではなく、GPIO の番号。
sw_pin = 25


# cf. http://mamerium.com/raspberry-pi-rpi-gpio-basic/


def main(args):
    signal.signal(signal.SIGINT, cleanup)
    signal.signal(signal.SIGTERM, cleanup)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(sw_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    interval = 0.1  # ボタン押下中のチェックインターバル(秒)
    shutdown_second = 3  # Shutdownまでのボタン押下時間(秒)
    max_counter = shutdown_second / interval
    print(max_counter)

    try:
        counter = 0
        while True:
            # 押した直後なのでゼロ
            state = GPIO.input(sw_pin)
            # 押しているときは０、それ以外で分岐。
            isClick = not (state)
            sysout("Switchの状態:{0}".format(isClick))
            sysout("Counter: [{0:3.1f}]".format(counter))  # 全体で3桁、小数点1桁

            if (isClick):  # 押してるときは
                counter += 1
                # 3秒おしぱなしだったら。
                if (counter > max_counter):
                    counter = 0
                    shutdownMessage = 'shutdownします'
                    speak( shutdownMessage )
                    sysout(shutdownMessage)
                    # return
                    subprocess.call('sudo shutdown -h now', shell=True)
                else:
                    time.sleep(interval)
            else:
                counter = 0
                # 押下待ちののタイムアウト時間(2000ms)。設定しておかないとアプリが終了できない
                GPIO.wait_for_edge(sw_pin, GPIO.FALLING, timeout=3000)
            # GPIO.wait_for_edge(sw_pin, GPIO.FALLING)

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
w