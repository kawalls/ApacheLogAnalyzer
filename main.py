import random
from datetime import datetime, timedelta
from collections import defaultdict
import re

FILENAME = "./test.log"

METHODS = ['GET', 'POST', 'DELETE']
RESOURCES = ['./index.html', 'login', '/dashboard', '/api/data']
RESPONSES = [200, 404, 500, 403]

class ApacheLA: # Apache Log Analyzer
    # default const parameters -> file

    def __init__(self, fileName):
        self.fileName = fileName
        self.log()

    def newFile(self, fileName):
        self.fileName = fileName
        self.file = open(fileName, "a")

    def log(self):
        self.log_data = {}
        pattern = r'(?P<ip>\S+) - - \[(?P<time>[^\]]+)\] "(?P<method>\S+) (?P<resource>\S+) \S+" (?P<status>\d{3})'

        data = open(self.fileName).read().splitlines()

        for x in range(len(data)):
            match = re.search(pattern, data[x])

            if match:
                if not match.group("ip") in self.log_data:
                    self.log_data[match.group("ip")] = Entries()

                self.log_data[match.group("ip")].entry_append(match.group("status"), match.group("resource"), match.group("method"))

class IPAddress:

    def __init__(self, octet1 = None, octet2 = None, octet3 = None, octet4 = None):
        if (octet1 is None):
            self.octet1 = random.randint(0, 255)
            self.octet2 = random.randint(0, 255)
            self.octet3 = random.randint(0, 255)
            self.octet4 = random.randint(0, 255)
            return

        self.octet1 = octet1
        self.octet2 = octet2
        self.octet3 = octet3
        self.octet4 = octet4


    def __str__(self):
        return f"{self.octet1}.{self.octet2}.{self.octet3}.{self.octet4}"
    
class Entries:

    def __init__(self):
        self.count = 0
        self.status = defaultdict(int)
        self.resources = defaultdict(int)
        self.methods = defaultdict(int)

    def entry_append(self, status, resource, method):
        self.status[status] += 1
        self.resources[resource] += 1
        self.methods[method] += 1
        self.count += 1
    
def generateLog(fileName, entries, ipAddresses = 5):

    # Entries = number of requests seen in log.
    # ipAddresses = number of randomized addresses

    file = open(fileName, "w")

    _randomAddresses = []

    for _ in range(ipAddresses):
        _randomIP = IPAddress()
        _randomAddresses.append(_randomIP)

    for x in range(entries):
        _randomIP = _randomAddresses[(random.randint(0, (ipAddresses - 1)))]
        _randomMethod = METHODS[(random.randint(0, (len(METHODS) - 1)))]
        _randomResponse = RESPONSES[(random.randint(0, (len(RESPONSES) - 1)))]
        _randomResource = RESOURCES[(random.randint(0, (len(RESOURCES) - 1)))]
        _randomDate = datetime.now()
        _randomDate -= timedelta(days=(random.randint(0, 30)))
        _randomDate -= timedelta(seconds=(random.randint(0, 86400)))
        _randomDateStr = _randomDate.strftime("[%d/%b/%Y:%H:%M:%S]")

        file.write(f'{_randomIP} - - {_randomDateStr} "{_randomMethod} {_randomResource} HTTP/1.1" {_randomResponse}\n')


    file.close()
    print(f'Random log "{fileName}" has been created.')

generateLog(FILENAME, 25, 2)

obj = ApacheLA(FILENAME)

print(f'{len(obj.log_data)} addresses found.')

for x in obj.log_data.keys():
    print(f'{x}')
