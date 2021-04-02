# IBus-python - Raspberry PI
Very simple script to read until 13 channels from IBus devices (i.e Flysky receivers)

## What: 
  Read data from ibus receivers with any device able to read serial ports (UART) - (i.e Raspberry Pi)

## How:
  Step 1: (Raspberry Pi Example) 
  Make sure to:
    - Activate serial interface on raspi-config
    - Python3 is installed and configured.
    - Connect your receiver's IBus pin to serial (UART) pin from raspberry pi. Usually it will show up on '/dev/serial' - If you have problems getting the interface to show on /dev try to add "dtoverlay=disable-bt" to /boot/config.txt and reboot
  
  
  Just run the script and change it to do whatever you want with the channel data.
  
  `sudo python3 ibus_reader.py`
  
  "sudo" rights are just to add permissions to read serial, otherwise it wont be needed.
  
  
  
  
  
