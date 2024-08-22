#!/bin/bash

sed -i "7c MMDVMBM=ON" /home/pi/status.ini

frecuencia=$(awk "NR==13" /home/pi/MMDVMHost/MMDVMBM.ini)
frecuencia=`expr substr $frecuencia 13 9`
sed -i "70c $frecuencia" /home/pi/status.ini

puerto=$(awk "NR==51" /home/pi/MMDVMHost/MMDVMBM.ini)
puerto=`expr substr $puerto 15 14`
sed -i "71c $puerto" /home/pi/status.ini

x=$(awk "NR==90" /home/pi/status.ini)

cd /home/pi/MMDVMHost
xterm -geometry 76x9+$x+258 -bg brown -fg white -fa 'serift' -fs 10x -T BRANDMEISTER -e sudo ./MMDVMBM MMDVMBM.ini &

 
