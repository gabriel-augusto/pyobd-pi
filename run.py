import bluetooth
import subprocess
import os
# import obd
import time

target_name = "OBDII"
target_address = None

while True:

    nearby_devices = bluetooth.discover_devices()

    print(nearby_devices)

    for device in nearby_devices:
        if target_name == bluetooth.lookup_name(device):
            target_address = device
            break

    if target_address is not None:
        print "found target bluetooth device with address ", target_address
        os.system("sudo rfcomm bind all")
        time.sleep(5)
        print "Connected!!!\n\n"
        """
        port = 1
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((target_address, port))
        """
        break
    else:
        print "could not find target bluetooth device nearby"

# connection = obd.OBD()
subprocess.Popen(["python", "obd_recorder.py"])
subprocess.Popen(["python", "log/obd_parser.py"])
subprocess.Popen(["python", "obd_gui.py"])
