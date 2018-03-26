import os
import sys


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
