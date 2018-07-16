import os
import sys
import subprocess

def cleanup(*args):
    sys.exit(0)


# inputがtargetsに含まれているかを確認する。
def contains(input, targets):
    #	sysout(targets)
    flag = False
    for target in targets:
        if (input == target):
            flag = True
    return flag


# flushしないと出力されないケースがあるため、必ずflushするprint文
def sysout(message):
    print(message)
    sys.stdout.flush()


# 非同期でしゃべる(未使用)
def speakAsync(message):
    print(message)
    sys.stdout.flush()
    subprocess.call('/home/pi/app/aquestalkpi/AquesTalkPi "' + message + '" | aplay &', shell=True)


# 同期でしゃべる
def speak(message):
    print(message)
    sys.stdout.flush()
    subprocess.call('/home/pi/app/aquestalkpi/AquesTalkPi "' + message + '" | aplay ', shell=True)