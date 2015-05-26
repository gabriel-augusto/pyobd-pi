from subprocess import call

call(["python","obd_recorder.py"])
call(["python","log/obd_parser.py"])
call(["python","obd_gui.py"])
