import glob
import os
import socket
import time as t
# from database import Database

REMOTE_SERVER = "www.google.com"


class LogParameters(dict):
    def __init__(self, placa, time, rpm, kmh, throttle, load, fuel_status):
        dict.__init__({})
        self['placa'] = placa
        self['time'] = time
        self['rpm'] = rpm
        self['kmh'] = kmh
        self['throttle'] = throttle
        self['load'] = load
        self['fuelStatus'] = fuel_status

    def __str__(self):
        return (
            "Placa: " + str(self['placa']) + ", Time: " + str(self['time']) + ", RPM: " + str(
                self['rpm']) + ", Km/h: " + str(
                self['kmh']) + ", Throttle: " + str(self['throttle']) + ", Load: " + str(
                self['load']) + ", Fuel Status: " + str(self['fuelStatus']))


class LogReader:
    def __init__(self):
        self.db = None
        self.log_list = []
        try:
            with open('placa.txt') as arc:
                self.placa = arc.readline().strip()
        except IOError as ioerr:
            print("\nIOerr: " + str(ioerr))

    @property
    def is_connected(self):
        try:
            host = socket.gethostbyname(REMOTE_SERVER)
            socket.create_connection((host, 80), 2)
            return True
        except:
            pass
        return False

    def read_log(self):
        # self.db = Database()
        for archive in glob.glob('*.log'):
            try:
                with open(archive) as arc:
                    text = arc.readlines()
            except IOError as ioerr:
                print("\nIOerr: " + str(ioerr))

            text.pop(0)
            i = 0
            for eachLine in text:
                if not i % 60:
                    parameters_list = eachLine.strip().split(',')
                    log_parameters = LogParameters(self.placa,
                                                   parameters_list[0],
                                                   parameters_list[1],
                                                   parameters_list[2],
                                                   parameters_list[3],
                                                   parameters_list[4],
                                                   parameters_list[5])
                    self.log_list.append(log_parameters)
                    # self.db.insert_parameters(log_parameters)
                i += 1
            os.remove(archive)
            print(str(self))
            # self.db.__del__()


    def __str__(self):
        string = ""
        return string.join([(str(x) + '\n') for x in self.log_list])


if __name__ == "__main__":
    reader = LogReader()
    while True:
        if reader.is_connected:
            reader.read_log()
        else:
            t.sleep(5)
