#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import csv
from datetime import datetime, timedelta
import json
import codecs
from csv import reader

FILE = os.path.dirname(os.path.abspath(__file__)) + r'/powerlog.csv'

time_offset = 3600 * 2

def get_data(daysback, type):
    data = []

    with open(FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            timestring = row[0] + "-" + row[1]
            datetime_object = datetime.strptime(timestring, '%m/%d/%Y-%H:%M:%S')
            d = datetime.today() - timedelta(days=daysback)
            if datetime_object > d:
                power = float(row[2])
                if power < 12000:
                    data.append([int((datetime_object.timestamp() + time_offset) * 1000), power])

    return data


def get_last(amount, type):
    data = get_data(1, type)[-amount:]
    output = "Time, Value\n"
    for line in data:
        datetime_object = datetime.fromtimestamp(line[0] / 1000) + time_offset
        output += str(datetime_object.strftime("%Y-%m-%dT%H:%M:%S.000Z")) + "," + str(line[1]) + "\n"
    return output



class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = self.path
        if path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            content = codecs.open("show.html", "r").read().encode('utf-8')
        elif path == "/daysback/power/1":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header("Access-Control-Allow-Origin", "*")
            jsonData = json.dumps(get_data(daysback=1, type=1))
            content = jsonData.encode('utf-8')
        elif path == "/daysback/power/7":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header("Access-Control-Allow-Origin", "*")
            jsonData = json.dumps(get_data(daysback=7, type=1))
            content = jsonData.encode('utf-8')
        elif path == "/last/1":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header("Access-Control-Allow-Origin", "*")
            jsonData = json.dumps(get_last(1, 1))
            content = jsonData.encode('utf-8')
        elif path == "/last/power/100":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header("Access-Control-Allow-Origin", "*")
            data = get_last(100, 1)
            content = data.encode('utf-8')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            content = "".encode('utf-8')

        self.end_headers()
        self.wfile.write(content)


httpd = HTTPServer(('', 80), SimpleHTTPRequestHandler)
httpd.serve_forever()
