#!/bin/bash
# sudo killall socat  
cd /home/pi/A108
sudo socat -d -d pty,link=/dev/virtual1,raw,echo=0 pty,link=/dev/virtual2,raw,echo=0 &

#sudo socat -d -d PTY,raw,echo=0,b9600,link=/dev/virtual1 PTY,raw,echo=0,b9600,link=/dev/virtual2

sudo python3 nextion_5.py &