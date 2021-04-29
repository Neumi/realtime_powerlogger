#!/usr/bin/env python3

import socket
import time
from datetime import datetime
import csv
import json
import os

logfile = os.path.dirname(os.path.abspath(__file__)) + r'/powerlog.csv'

last_time = time.time()
UDP_IP = '0.0.0.0'
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
	try:
		data, addr = sock.recvfrom(1024)
		print(data)
		# print("received message: %s" % data)
		# print("device: ",  addr)
		data_json = json.loads(data)
		# print(data_json)
		elapsed_time = float(data_json["last_ping"] / 1000)
		power_draw = 3600.0 / elapsed_time
		# print("elapsed time", elapsed_time)
		# print("power usage in Watt:  " + str(power_draw) +  " W")
		# print()
		with open(logfile, 'a') as f:
			now = datetime.now()
			date = now.strftime('%m/%d/%Y')
			date_time = now.strftime('%H:%M:%S')
			fields = [date, date_time, str(round(power_draw, 2))]
			writer = csv.writer(f)
			writer.writerow(fields)

	except:
		print("something went wrong!")
		exit()
