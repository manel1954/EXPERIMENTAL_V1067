#!/bin/bash
 
                        cd /home/pi/Downloads
                        
                        wget https://github.com/rustdesk/rustdesk/releases/download/1.3.2/rustdesk-1.3.2-armv7-sciter.deb
                        
                        sudo dpkg -i rustdesk-1.3.2-armv7-sciter.deb

                        sudo apt -f install

                        sudo rm rustdesk-1.3.2-armv7-sciter.deb*
