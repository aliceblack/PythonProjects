from tello import Tello
import sys
from datetime import datetime
import time

#Perform a list of drone movements
commands = [ "command", "takeoff", "land" ]

tello = Tello()
for command in commands:
    if command.find('delay') != -1:
        sec = float(command.partition('delay')[2])
        print('delay %s' % sec)
        time.sleep(sec)
        pass
    else:
        tello.send_command(command)

log = tello.get_log()
out = open('log/logfile.txt', 'w')
for stat in log:
    str = stat.return_stats()
    out.write(str)