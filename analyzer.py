from collections import defaultdict
from logGenerator import generateLog
import re

FILENAME = "./test.log"

class ApacheLA: # Apache Log Analyzer
    # default const parameters -> file

    def __init__(self, fileName):
        self.fileName = fileName
        self.log()

    def newFile(self, fileName):
        self.fileName = fileName
        self.log()

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

generateLog(FILENAME, 25, 4)

obj = ApacheLA(FILENAME)

print(f'{len(obj.log_data)} addresses found.')

for x in obj.log_data.keys():
    print(f'{x}')

# What to add: Better display of IPAddresses & stats