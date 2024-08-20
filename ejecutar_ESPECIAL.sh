#!/bin/bash

frecuencia=$(awk "NR==13" /home/pi/MMDVMHost/MMDVMESPECIAL.ini)
frecuencia=`expr substr $frecuencia 13 9`
sed -i "74c $frecuencia" /home/pi/status.ini

puerto=$(awk "NR==51" /home/pi/MMDVMHost/MMDVMESPECIAL.ini)
puerto=`expr substr $puerto 15 14`
sed -i "75c $puerto" /home/pi/status.ini

x=$(awk "NR==92" /home/pi/status.ini)

cd /home/pi/MMDVMHost
xterm -geometry 76x10+$x+64  -bg black -fg yellow -fa 'arial' -fs 10x -T ESPECIAL -e sudo ./MMDVMESPECIAL MMDVMESPECIAL.ini &