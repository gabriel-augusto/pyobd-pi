from subprocess import Popen

Popen(["python","obd_recorder.py"])
Popen(["python","log/obd_parser.py"])
Popen(["python","obd_gui.py"])
