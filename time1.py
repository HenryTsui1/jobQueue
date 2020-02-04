'''
Name: Henry Tsui
Student ID: 20105575
'''

import time
import datetime

def calctime(job_queue): #converts the timestamp into unix time format, to calculate the time difference
    t = datetime.datetime.strptime(job_queue[0][-1], "%a %b %d %H:%M:%S %Y")  #formats into unix time
    current = time.time() #sets current time
    timediff = current - t.timestamp() #calculates the time difference, to show how long it takes to complete a 'task'
    return timediff


def sleep(cmds):
    cmds[1] = int(cmds[1]) 
    time.sleep(cmds[1]) #pauses the program from the time specified

