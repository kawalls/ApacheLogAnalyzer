import random
from datetime import datetime, timedelta

METHODS = ['GET', 'POST', 'DELETE']
RESOURCES = ['./index.html', 'login', '/dashboard', '/api/data']
RESPONSES = [200, 404, 500, 403]

def generateLog(fileName, entries, ipAddresses = 5):

    # Entries = number of requests seen in log.
    # ipAddresses = number of randomized addresses

    file = open(fileName, "w")

    _randomAddresses = []

    for _ in range(ipAddresses):
        _randomIP = f"{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
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